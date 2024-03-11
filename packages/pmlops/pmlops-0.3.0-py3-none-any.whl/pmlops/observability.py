"""
Observability module to store observability metrics

This module contains the ObservabilityReport class to store observability metrics
"""

from abc import ABC, abstractmethod
from typing import List

import pandas as pd
from evidently import ColumnMapping
from evidently.metrics import (
    ColumnDriftMetric,
    DatasetDriftMetric,
    DatasetMissingValuesMetric,
)
from evidently.report import Report
from sklearn.metrics import accuracy_score


class ModelPerformance:
    """
    Performance class to store performance metrics
    """

    def __init__(self, dataframe: pd.DataFrame) -> None:
        """
        Initialize the class

        Args:
        dataframe (pd.DataFrame): The dataset
        """
        self.accuracy = self.calculate_accuracy(dataframe)

    def calculate_accuracy(self, dataset: pd.DataFrame) -> float:
        """
        Calculate accuracy

        Args:
        dataset (pd.DataFrame): The dataset

        Returns:

        float: The accuracy
        """
        return accuracy_score(dataset["target"], dataset["real_value"])


class ReportBuilder(ABC):
    """
    ReportBuilder class to create reports
    """

    @abstractmethod
    def add_drift_measurement(self):
        """
        Add drift measurement
        """
        pass

    @abstractmethod
    def add_performance_measurement(self):
        """
        Add performance measurement
        """
        pass

    @abstractmethod
    def add_missing_values_measurement(self):
        """
        Add missing values measurement
        """
        pass


class ObservabilityReportBuilder(ReportBuilder):
    """
    Observability class to store observability metrics
    """

    def __init__(self, features: List, target: str) -> None:
        """
        Initialize the class

        Args:
        features (List): The features
        target (str): The target
        """
        self.metrics = []
        self.mapping = ColumnMapping(
            prediction=target, numerical_features=features, categorical_features=[], target=None
        )
        self.performance = None

    def add_drift_measurement(self, stattest: str = "psi") -> None:
        """
        Add drift measurement

        Args:
        stattest (str, optional): Statistical test. Defaults to "psi".
        """
        self.metrics.append(
            DatasetDriftMetric(
                stattest=stattest,
            )
        )

    def add_single_drift_measurement(self, stattest: str = "psi") -> None:
        """
        Add single drift measurement

        Args:
        stattest (str, optional): Statistical test. Defaults to "psi".
        """
        for feature in self.features:
            self.metrics.append(ColumnDriftMetric(column=feature, stattest=stattest))

    def add_missing_values_measurement(self) -> None:
        """
        Add missing values measurement
        """
        self.metrics.append(DatasetMissingValuesMetric())

    def add_performance_measurement(self, dataset: pd.DataFrame) -> None:
        """
        Add performance measurement

        Args:
        dataset (pd.DataFrame): The dataset
        """
        performance = ModelPerformance(dataframe=dataset)
        self.performance = performance

    def run(self, reference_data: pd.DataFrame, production_data: pd.DataFrame) -> None:
        """
        Run the report

        Args:
        reference_data (pd.DataFrame): The reference data
        production_data (pd.DataFrame): The production data

        Raises:
        ValueError: No metrics added to the report
        """

        if self.metrics == []:
            raise ValueError("No metrics added to the report")
        else:
            report = Report(metrics=self.metrics)
            report.run(
                reference_data=reference_data,
                current_data=production_data,
                column_mapping=self.mapping,
            )
            _results = report.as_dict()
            num_drifted_columns = _results["metrics"][0]["result"]["number_of_drifted_columns"]
            share_missing_values = _results["metrics"][1]["result"]["current"][
                "share_of_missing_values"
            ]
            model_performance = self.performance.accuracy
        return {
            "num_drifted_columns": num_drifted_columns,
            "share_missing_values": share_missing_values,
            "model_performance": model_performance,
        }
