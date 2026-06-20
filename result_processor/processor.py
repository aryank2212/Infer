import re


class ResultProcessor:

    def clean(
        self,
        text
    ):

        text = re.sub(
            r"<think>.*?</think>",
            "",
            text,
            flags=re.DOTALL
        )

        return text.strip()