import random

from noises.noise_generator import ProceduralGenerator
from utils import normalized


class WhiteNoiseGenerator(ProceduralGenerator):
	def generate(self) -> [[float]]:
		"""
		Devuelve una matriz con los datos generados por el ruido
		:return: matriz de datos
		"""
		data = [[random.random() for _ in range(self._size)] for _ in range(self._size)]
		if self._normalized:
			data = normalized(data)
		return data
