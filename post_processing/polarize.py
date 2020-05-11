from post_processing.post_process import PostProcess


class Polarize(PostProcess):
	"""
	Este postproceso polariza la entrada, convirtiendo en 0 todos los valores inferiores a un umbral y a 1 el resto
	"""

	def __init__(self, data, threshold=0.5):
		super().__init__(data)
		self._threshold = threshold

	def do_work(self) -> [[float]]:
		"""
		Realiza su trabajo
		:param data: Datos a transformar
		:return: Datos transformados
		"""
		return [[1.0 if self._data[x][y] >= self._threshold else 0.0 for x in range(len(self._data[0]))] for y in range(len(self._data))]

	def __str__(self):
		return self.__class__.__name__
