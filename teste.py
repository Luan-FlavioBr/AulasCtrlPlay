from matematica import geometria
from matematica import probabilidade

# Testando funções do módulo geometria
print("Área do círculo de raio 5:", geometria.area_circulo(5))
print("Área do retângulo de largura 4 e altura 6:", geometria.area_retangulo(4, 6))
print("Perímetro do triângulo de lados 3, 4, 5:", geometria.perimetro_triangulo(3, 4, 5))
print("Área do triângulo de lados 3, 4, 5:", geometria.area_triangulo(3, 4, 5))

# Testando funções do módulo probabilidade
print("Média dos números [1, 2, 3, 4, 5]:", probabilidade.media([1, 2, 3, 4, 5]))
print("Moda dos números [1, 2, 2, 3, 4]:", probabilidade.moda([1, 2, 2, 3, 4]))

