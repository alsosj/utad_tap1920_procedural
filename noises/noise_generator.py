class ProceduralGenerator:
	def __init__(self, octaves, size, normalized=True):
		"""
		Constructor
		"""
		self._octaves = octaves
		self._freq = 16 * self._octaves
		self._size = size
		self._normalized = normalized

	def generate(self) -> [[float]]:
		"""
		Devuelve una matriz con los datos generados por el ruido
		:return: matrix de datos
		"""
		return [[]]
