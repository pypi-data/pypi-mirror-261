""" Anonimity evaluator module """

import os
from typing import List, Tuple

import matplotlib.pyplot as plt
import pandas as pd
from anonymeter.evaluators import InferenceEvaluator, SinglingOutEvaluator
from anonymeter.stats.confidence import EvaluationResults


class AnonymityEvaluator:
    """
    A class for evaluating the anonymity of datasets by performing various
    evaluations, including singling out evaluations in both univariate and
    multivariate contexts.
    """

    def __init__(
        self, ori: pd.DataFrame, syn: pd.DataFrame, control: pd.DataFrame
    ) -> None:
        """
        Initializes the AnonymityEvaluator with original, synthetic, and control datasets.

        Parameters:
        - ori: The original dataset.
        - syn: The synthetic dataset generated as an anonymized version of the original dataset.
        - control: A control dataset used for comparison.
        """
        self.ori = ori
        self.syn = syn
        self.control = control

    def univariate_single_out_evaluator(self, n_attacks: int = 500) -> None:
        """
        Evaluates the risk of singling out individuals using univariate attacks.

        Parameters:
        - n_attacks: The number of attack iterations to perform. Default is 500.
        """
        print("// Univariate Single out //")
        evaluator = SinglingOutEvaluator(
            ori=self.ori, syn=self.syn, control=self.control, n_attacks=n_attacks
        )

        try:
            evaluator.evaluate(mode="univariate")
            risk = evaluator.risk()
            print(f"**Risk:** {risk}")

        except RuntimeError as ex:
            print(
                f"**Error:** Singling out evaluation failed with {ex}. Please re-run this cell. "
                "For more stable results increase `n_attacks`. Note that this will "
                "make the evaluation slower."
            )

        evaluator.risk(confidence_level=0.95)

        res = evaluator.results()

        print("**Success Rate of Main Attack:**", res.attack_rate)
        print("**Success Rate of Baseline Attack:**", res.baseline_rate)
        print("**Success Rate of Control Attack:**", res.control_rate)

        print(f"**Risk:** {res.risk()}")

        print("\n")

    def multivariate_single_out_evaluator(
        self, n_attacks: int = 100, n_cols: int = 4
    ) -> None:
        """
        Evaluates the risk of singling out individuals using multivariate attacks.

        Parameters:
        - n_attacks: The number of attack iterations to perform. This attack takes longer.
        Default is 100.
        - n_cols: The number of columns to use in the attack. Default is 4.
        """
        print("// Multivariate Single out //")

        evaluator = SinglingOutEvaluator(
            ori=self.ori,
            syn=self.syn,
            control=self.control,
            n_attacks=n_attacks,
            n_cols=n_cols,
        )

        try:
            evaluator.evaluate(mode="multivariate")
            risk = evaluator.risk()
            print(f"**Risk:** {risk}")

        except RuntimeError as ex:
            print(
                f"**Error:** Singling out evaluation failed with {ex}. Please re-run this cell. "
                "For more stable results increase `n_attacks`. Note that this will "
                "make the evaluation slower."
            )

        print("\n")

    def inference_risk_evaluator(self, n_attacks: int = 100) -> None:
        """
        Evaluates and visualizes the inference risk of each column in the dataset.

        This method iterates through each column in the original dataset, treating it
        as a secret to be protected. It then evaluates the inference risk associated
        with each secret column using an InferenceEvaluator, considering all other
        columns as auxiliary information.

        Parameters:
        - n_attacks: int = 1000
            The number of attack simulations to run for each secret column. Defaults to 1000.

        Outputs:
        - A bar chart saved to "../report/anonymity_evaluation/inference_risk.png" visualizing
          the inference risk associated with each column.
        - Prints a message indicating the location of the saved image.
        """
        columns = self.ori.columns
        results: List[Tuple[str, EvaluationResults]] = []

        for secret in columns:
            aux_cols = [col for col in columns if col != secret]

            evaluator = InferenceEvaluator(
                ori=self.ori,
                syn=self.syn,
                control=self.control,
                aux_cols=aux_cols,
                secret=secret,
                n_attacks=n_attacks,
            )
            evaluator.evaluate(n_jobs=-2)
            results.append((secret, evaluator.results()))

        fig, ax = plt.subplots()
        risks = [res[1].risk().value for res in results]
        columns = [res[0] for res in results]

        ax.bar(x=columns, height=risks, alpha=0.5, ecolor="black", capsize=10)
        plt.xticks(rotation=45, ha="right")
        ax.set_ylabel("Measured inference risk")
        _ = ax.set_xlabel("Secret column")

        plt.savefig("../report/anonymity_evaluation/inference_risk.png")
        print("See the image in the report folder.")

    def evaluate(
        self,
        univariate_n_attacks: int = 500,
        multivariate_n_attacks: int = 100,
        inference_n_attacks: int = 100,
        n_cols: int = 4,
    ) -> None:
        """
        Runs both univariate and multivariate single out evaluations.

        Parameters:
        - univariate_n_attacks: The number of univariate attack iterations to perform.
        Default is 500.
        - multivariate_n_attacks: The number of multivariate attack iterations to perform.
        Default is 100.
        - n_cols: The number of columns to use in the multivariate attack. Default is 4.
        """
        report_path = os.path.join("..", "report", "anonymity_evaluation")
        if not os.path.exists(report_path):
            try:
                os.makedirs(report_path)
            except FileExistsError:
                pass

        print("//// Anonymity Evaluation ////")
        print("\n")

        print("/// Singling out ///")
        self.univariate_single_out_evaluator(n_attacks=univariate_n_attacks)
        self.multivariate_single_out_evaluator(
            n_attacks=multivariate_n_attacks, n_cols=n_cols
        )

        print("/// Inference Risk ///")
        self.inference_risk_evaluator(n_attacks=inference_n_attacks)

        print("\n\n")
