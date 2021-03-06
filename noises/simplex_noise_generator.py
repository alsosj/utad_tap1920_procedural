from noise import snoise2

from noises.noise_generator import ProceduralGenerator
from utils import normalized


class SimplexNoiseGenerator(ProceduralGenerator):
	def generate(self) -> [[float]]:
		"""
		Devuelve una matriz con los datos generados por el ruido
		:return: matriz de datos
		"""
		data = [
			[
				snoise2(x / self._freq, y / self._freq, self._octaves) for x in range(self._size)
			] for y in range(self._size)]
		if self._normalized:
			data = normalized(data)
		return data
