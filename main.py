from noises.white_noise_generator import WhiteNoiseGenerator
from output_generators.image_generator import ImageGenerator
from noises.perlin_noise_generator import PerlinNoiseGenerator
from noises.simplex_noise_generator import SimplexNoiseGenerator
from output_generators.json_generator import JsonGenerator
from post_processing.cellular import CellularAutomata
from post_processing.polarize import Polarize
from post_processing.soften import Soften
from utils import normalized

print('Bienvenido a la aplicación de pruebas de algoritmos procedimentales')

# Paso 1: Creación de los datos
print('Paso 1: generación del ruido base')
generator = SimplexNoiseGenerator(4, 1024, True)
data = generator.generate()

data = normalized(data)
# Paso 2: Procesamiento adicional
print('Paso 2: procesamiento adicional')
post = Polarize(data)
data = post.do_work()
# Paso 3: Creación de la imagen a partir de los datos finales
print('Paso 3: exportando datos')
out_gen = ImageGenerator(data, 'output.png', (0, 0, 255), (255, 0, 0))
out_gen.generate_output()
