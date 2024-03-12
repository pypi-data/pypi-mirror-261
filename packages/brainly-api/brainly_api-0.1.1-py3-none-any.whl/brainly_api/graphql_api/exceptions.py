from .responses import BrainlyGraphqlResponse


class BrainlyGraphqlException(Exception):
    def __init__(
        self,
        message,
        response: BrainlyGraphqlResponse | None = None,
        query: str | None = None,
        variables: str | None = None
    ):
        self.message = message
        self.response_errors = response.errors if response else []
        self.query = query
        self.variables = variables

        super().__init__(
            self.message if len(self.response_errors) == 0 else f"{self.message}: {self.response_errors}"
        )
