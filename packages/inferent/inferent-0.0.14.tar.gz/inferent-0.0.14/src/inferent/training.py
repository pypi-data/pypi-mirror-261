"""Utilities for model preprocessing, training, and testing"""

# TODO: convert to python3 syntax!

from contextlib import contextmanager
import copy
from dataclasses import dataclass
import joblib
import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader, TensorDataset
from torch.utils.tensorboard import SummaryWriter

@dataclass
class ModelPackage:
    preprocessor: Preprocessor
    model: any
    metadata: dict

class Preprocessor:
    """Class responsible for preprocessing data"""

    logger = logging.getLogger("Preprocessor")
    categorical_map = {}
    input_features = None
    processed_featurelist = None
    xencoder = None
    xscaler = None
    yscaler = None
    clip_dict = None

    def __init__(self, clip_dict=None):
        self.clip_dict = clip_dict

    def register_categorical(self, data, cols, one_hot=True):
        """adds categorical cols `cols` to a separate datastore

        Will replace cols with their one hot encoded values
        """
        # TODO: embeddings
        for col in cols:
            # Get categorical column
            cat = data[[col]]  # [[ ]] to return df not series
            if one_hot:
                self.xencoder = OneHotEncoder()
                self.xencoder.fit(cat)
                codes = self.xencoder.transform(cat).toarray()
                feature_names = self.xencoder.get_feature_names_out(
                    cat.columns
                )
                # `cat` is now the encoded categorical column
                cat = pd.DataFrame(
                    codes, columns=feature_names, index=cat.index
                ).astype(int)
                data = pd.concat(
                    [
                        data.drop(columns=[col]),
                        pd.DataFrame(
                            codes, columns=feature_names, index=cat.index
                        ).astype(int),
                    ],
                    axis=1,
                )
                self.categorical_map[col] = feature_names
            else:
                self.categorical_map[col] = col
        self.processed_featurelist = list(data.columns)
        return data

    def register_xscaler(self, xdata, scaler="minmax"):
        """normalizes data"""
        if scaler == "minmax":
            self.xscaler = MinMaxScaler()
            self.yscaler = MinMaxScaler()
        else:
            raise ValueError("Improper input for `scaler`.")

        self.xscaler.fit(xdata)

    def register_yscaler(self, ydata, scaler="minmax"):
        """normalizes data"""
        if scaler == "minmax":
            self.yscaler = MinMaxScaler()
        else:
            raise ValueError("Improper input for `scaler`.")

        self.yscaler.fit(ydata)

    def clip(self, xdata):
        for to_find, clip in self.clip_dict.items():
            cols = [col for col in xdata.columns if to_find in col]
            xdata[cols] = xdata[cols].clip(upper=clip)

        return xdata

    def preprocess_x(self, xdata, clip=True, encode=True, scale=True):
        if clip:
            xdata = self.clip(xdata)

        # Encoding
        if encode and len(self.categorical_map) > 0:
            cat = xdata[self.categorical_map.keys()]
            codes = self.xencoder.transform(cat).toarray()
            feature_names = self.xencoder.get_feature_names_out(cat.columns)
            cat = pd.DataFrame(
                codes, columns=feature_names, index=cat.index
            ).astype(int)
            xdata = pd.concat(
                [
                    xdata.drop(columns=[self.categorical_map.keys()]),
                    pd.DataFrame(
                        codes, columns=feature_names, index=cat.index
                    ).astype(int),
                ],
                axis=1,
            )

        # Scaling
        if scale:
            xdata = self.xscaler.transform(xdata)

        return xdata

class Predictor:
    m = None

    def __init__(
        self, model_package: ModelPackage = None, model_path: str = None
    ):
        if model_package is not None:
            self.m = model_package
        elif model_path is not None:
            self.m = ModelPackage(None)

    def predict(
        self,
        xdata: pd.DataFrame,
        use_processed_featurelist=False,
        encode=True,
        scale=True,
    ):
        if not use_processed_featurelist:
            # reduce down to features in features list
            xdata = xdata[self.m.metadata["featurelist"]]
        else:
            xdata = xdata[self.m.preprocessor.processed_featurelist]

        # preprocess
        xdata = self.m.preprocessor.preprocess_x(
            xdata, encode=encode, scale=scale
        )

        # predict
        with evaluating(self.m.model), torch.no_grad():
            return self.m.model(torch.tensor(xdata, dtype=torch.float32))


class DataManager:
    """Takes a pd.DataFrame as input and manages it for training.

    Performs preprocessing tasks.
    """

    logger = logging.getLogger("DataManager")
    raw_data = None
    data = None
    preprocessor = None
    Xdf_train = None
    Xdf_vld = None
    Xdf_test = None
    ydf_train = None
    ydf_vld = None
    ydf_test = None
    X_train = None
    X_vld = None
    X_test = None
    y_train = None
    y_vld = None
    y_test = None

    def __init__(self, raw_data, label_col, clip_dict=None, seed=None):
        self.raw_data = raw_data.copy()
        self.xdata = raw_data.drop(columns=[label_col])
        self.ydata = raw_data[[label_col]]  # [[ ]] to return df, not series
        self.preprocessor = Preprocessor(clip_dict)
        self.seed = seed
        self.label_col = label_col

    def drop_nans(self):
        """performs bifurcated self.raw_data.dropna() with some logging"""
        nan_cols = [
            col
            for col in self.raw_data.columns
            if self.raw_data[col].isna().sum() > 0
        ]
        nans = self.raw_data[self.raw_data[nan_cols].isna().any(axis=1)]
        self.logger.info(
            "%s rows of data with NaNs: %s \n %s", len(nans), nan_cols, nans
        )
        self.xdata = self.xdata.drop(nans.index)
        self.ydata = self.ydata.drop(nans.index)

    def split(
        self, vld_size=0.1, tst_size=0.1, vld_shuffle=True, tst_shuffle=False
    ):
        """Splits into train, test, and validation"""
        if tst_size > 0:
            Xdf_temp, self.Xdf_test, ydf_temp, self.ydf_test = (
                train_test_split(
                    self.xdata,
                    self.ydata,
                    test_size=tst_size,
                    random_state=self.seed,
                    shuffle=tst_shuffle,
                )
            )
        else:
            self.Xdf_test, self.ydf_test = pd.DataFrame(), pd.DataFrame()
            Xdf_temp, ydf_temp = self.xdata, self.ydata

        self.Xdf_train, self.Xdf_vld, self.ydf_train, self.ydf_vld = (
            train_test_split(
                Xdf_temp,
                ydf_temp,
                test_size=vld_size / (1.0 - tst_size),
                random_state=self.seed,
                shuffle=vld_shuffle,
            )
        )

    def clip(self):
        self.xdata = self.preprocessor.clip(self.xdata)

    def encode(self, cols):
        self.xdata = self.preprocessor.register_categorical(self.xdata, cols)

    def normalize(self, scaler="minmax"):
        self.preprocessor.register_xscaler(self.Xdf_train, scaler)
        self.preprocessor.register_yscaler(self.ydf_train, scaler)

        self.X_train = self.preprocessor.xscaler.transform(self.Xdf_train)
        self.X_vld = self.preprocessor.xscaler.transform(self.Xdf_vld)
        self.X_test = (
            self.preprocessor.xscaler.transform(self.Xdf_test)
            if not self.Xdf_test.empty
            else np.array([])
        )
        self.y_train = self.preprocessor.yscaler.transform(self.ydf_train)
        self.y_vld = self.preprocessor.yscaler.transform(self.ydf_vld)
        self.y_test = (
            self.preprocessor.yscaler.transform(self.ydf_test)
            if not self.ydf_test.empty
            else np.array([])
        )

        # TODO: only for binary clasification
        # self.logger.info(
        #    (
        #        self.ydf_vld.to_numpy() == self.preprocessor.yscaler.transform(self.ydf_vld)
        #    ).all()
        # )  # sanity check :)
        # self.logger.info(
        #    (
        #        self.ydf_test.to_numpy()
        #        == self.preprocessor.yscaler.transform(self.ydf_test)
        #    ).all()
        # )  # sanity check :)

    def get_pytorch_trainloader(self, batch_size=64, shuffle=True):
        """Get TrainLoader"""
        # TODO: dtypes
        # TODO: Dataset must fit in memory; if not, must use Streaming Data
        # Loader
        trainset = TensorDataset(
            torch.tensor(self.X_train, dtype=torch.float32),
            torch.tensor(self.y_train, dtype=torch.int),
        )
        return DataLoader(trainset, batch_size=batch_size, shuffle=shuffle)


class TorchModule(torch.nn.Module):
    """Pytorch module"""

    def __init__(self):
        super().__init__()
        # TODO: make this configurable by children
        self.install_hooks()

    def install_hooks(self, output=True):
        """Install hooks (configurable)"""
        if output:
            _ = torch.nn.modules.module.register_module_forward_hook(
                self.save_output_hook
            )

    def save_output_hook(self, module, _, output):
        """save any modules output in an attribute"""
        module.forward_output = output

    def forward(self):
        """forward"""
        raise NotImplementedError("forward not implemented")


@contextmanager
def evaluating(net):
    """Temporarily switch to evaluation mode.

    Affects modules such as batchnorm and dropout.
    """
    istrain = net.training
    try:
        net.eval()
        yield net
    finally:
        if istrain:
            net.train()


class Trainer:
    """Model trainer class"""

    logger = logging.getLogger("Trainer")
    epoch = 0

    def __init__(
        self,
        name,
        datamgr,
        model,
        loss_fn,
        metrics,
        optimizer="adam",
        batch_size=64,
        max_epochs=50,
        lr=0.001,
    ):
        self.datamgr = datamgr
        self.model = model
        self.loss_fn = loss_fn
        self.metrics = metrics
        self.batch_size = batch_size
        self.max_epochs = max_epochs
        self.writer = SummaryWriter(name)
        if optimizer == "adam":
            self.optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        else:
            raise ValueError(f"Invalid optimizer {optimizer}")

    def write(self, name, x):
        """Write to summarywriter"""
        if x is None:
            self.logger.info("x is None. Not writing.")
            return
        if isinstance(x, torch.Tensor) and x.numel() > 1:
            self.writer.add_histogram(name, x, self.epoch)
        else:
            self.writer.add_scalar(
                name,
                x.item() if isinstance(x, torch.Tensor) else x,
                self.epoch,
            )

    def write_stdratio(self, name, x, y):
        """Write ratio of std to summarywriter"""
        if x is None or y is None:
            self.logger.info("x (%s) or y(%s) is None. Not writing.", x, y)
            return
        if isinstance(x, torch.Tensor) and x.numel() > 1:
            self.writer.add_histogram(name, x.std() / y.std(), self.epoch)
        else:
            self.writer.add_scalar(name, x.std() / y.std(), self.epoch)

    def train(self):
        """train"""
        self.logger.info(
            "Model has %s parameters",
            sum(x.reshape(-1).shape[0] for x in self.model.parameters()),
        )
        batch_idx = 0

        trainloader = self.datamgr.get_pytorch_trainloader(
            batch_size=self.batch_size, shuffle=True
        )

        best_acc = np.inf  # init to negative infinity
        best_weights = None
        best_epoch = -1
        self.epoch = 0
        trn_metrics = copy.deepcopy(self.metrics)
        vld_metrics = copy.deepcopy(self.metrics)

        self.logger.info("Starting to train")
        for _ in range(self.max_epochs):
            trn_metrics.reset()
            vld_metrics.reset()
            for batch in trainloader:
                batch_idx += 1
                X, y = batch
                preds = self.model(X)
                with evaluating(self.model), torch.inference_mode():
                    metrics_output = trn_metrics.update(
                        preds.squeeze(), y.squeeze()
                    )
                    vld_preds = self.model(
                        torch.tensor(self.datamgr.X_vld, dtype=torch.float32)
                    )
                    vld_metrics_output = vld_metrics.update(
                        vld_preds.squeeze(),
                        torch.tensor(
                            self.datamgr.y_vld, dtype=torch.int
                        ).squeeze(),
                    )

                loss_val = self.loss_fn(preds, y.type(torch.float32))
                self.optimizer.zero_grad()
                loss_val.backward()
                self.optimizer.step()

            for metric, metric_output in metrics_output.items():
                self.write(f"metrics/{metric}", metric_output[1])
            for metric, metric_output in vld_metrics_output.items():
                self.write(f"vld_metrics/{metric}", metric_output[1])
            # TODO: optimizer
            # self.model.write("learning_rate", optimizer.lr, scal=True)
            # logger.info(f"state_dict {optimizer.state_dict()}")

            moduledict = {}
            for name, module in self.model.named_modules():
                instancenum = moduledict.get(name, 0) + 1
                moduledict[name] = instancenum
                if isinstance(module, torch.nn.Linear):
                    self.write(f"linear{instancenum}/weights", module.weight)
                    self.write(
                        f"linear{instancenum}/weights/grad", module.weight.grad
                    )
                    self.write_stdratio(
                        f"linear{instancenum}/grad-data-ratio",
                        module.weight.grad,
                        module.weight,
                    )
                    self.write(f"linear{instancenum}/bias", module.bias)
                    self.write(
                        f"linear{instancenum}/bias/grad", module.bias.grad
                    )
                    self.write(
                        f"linear{instancenum}/output", module.forward_output
                    )
                elif isinstance(module, torch.nn.LayerNorm):
                    self.write(
                        f"layernorm{instancenum}/weights", module.weight
                    )
                    self.write(
                        f"layernorm{instancenum}/weights/grad",
                        module.weight.grad,
                    )
                    self.write(f"layernorm{instancenum}/bias", module.bias)
                    self.write(
                        f"layernorm{instancenum}/bias/grad", module.bias.grad
                    )
                    # TODO: check if output exists
                    self.write(
                        f"layernorm{instancenum}/output", module.forward_output
                    )

            def _get_metrics_str(metrics_output):
                return " | ".join(
                    [
                        metric + f" {metric_output[1]:,.2f}"
                        for metric, metric_output in metrics_output.items()
                    ]
                )

            self.logger.info(
                "\033[33mEpoch %s, trn: %s \033[0m",
                self.epoch,
                _get_metrics_str(metrics_output),
            )
            self.logger.info(
                "\033[32mEpoch %s, vld: %s \033[0m",
                self.epoch,
                _get_metrics_str(vld_metrics_output),
            )
            if vld_metrics_output["Binary Cross Entropy"][1] < best_acc:
                best_acc = vld_metrics_output["Binary Cross Entropy"][1]
                best_weights = copy.deepcopy(self.model.state_dict())
                best_epoch = self.epoch
            self.epoch += 1

        self.logger.info(
            "Best model found in epoch %s with BCE %s.", best_epoch, best_acc
        )
        self.model.load_state_dict(best_weights)
