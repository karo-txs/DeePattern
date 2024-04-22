
from deepattern.patterns.builder.builder import ModelBuilder


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> ModelBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ModelBuilder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled model.
        """
        self._builder = builder

    """
    The Director can construct several model variations using the same
    building steps.
    """

    def build_layer_based_model(self) -> None:
        self.builder.include_input()
        self.builder.include_hidden()
        self.builder.include_output()
        self.builder.compile()
        
    def build_model(self) -> None:
        self.builder.compile()
