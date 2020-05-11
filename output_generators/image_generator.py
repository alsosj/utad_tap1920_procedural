import numpy as np
from PIL import Image, ImageDraw

from output_generators.output_generator import OutputGenerator
from utils import normalized_val


class ImageGenerator(OutputGenerator):
	"""
	Guarda los datos en una imagen
	"""
	def __init__(self, data: [[float]], path: str, min_color=(0, 0, 0), max_color=(255, 255, 255)):
		"""
		Constructor
		:param data: datos a representar
		:param path: ruta del fichero a crear
		:param min_color: color asociado al valor mínimo de data
		:param max_color: color asociado al valor máximo de data
		"""
		super().__init__(data, path)
		self._min_color = min_color
		self._max_color = max_color
		self.__min_value = np.min(data)
		self.__max_value = np.max(data)

	def generate_output(self) -> None:
		"""
		Genera una imagen a partir de una matriz de datos
		"""
		# (0, 0) = esquina superior izquierda
		img = Image.new('RGB', (len(self._data), len(self._data[0])))
		draw = ImageDraw.Draw(img)
		for y, row in enumerate(self._data):
			for x, value in enumerate(row):
				draw.point((x, y), fill=self.get_target_color(value))
		del draw

		img.save(self._path)

	def get_target_color(self, val: float) -> (int, int, int):
		"""
		Obtiene el color correspondiente a un valor.
		Será max_color si el valor es el valor máximo de self._data,
		min_color si es el valor mínimo y uno intermedio en otro caso
		:param val: valor del que queramos obtener el color
		:return: color RGB con valoers en el rango 0-255
		"""
		normalized = normalized_val(val, self.__min_value, self.__max_value)
		target_r = int((self._max_color[0] - self._min_color[0]) * normalized + self._min_color[0])
		target_g = int((self._max_color[1] - self._min_color[1]) * normalized + self._min_color[1])
		target_b = int((self._max_color[2] - self._min_color[2]) * normalized + self._min_color[2])
		return target_r, target_g, target_b
