# Juego de Batalla RPG

Un juego de batalla por turnos hecho en Python.

---

## Que es el juego

Es un juego donde dos personajes pelean por turnos. Uno ataca, luego el otro ataca, y así hasta que uno de los dos se queda sin vida. Dependiendo del tipo de personaje, el ataque es diferente.

---

## Tipos de Personajes

### Guerrero
- Ataca mas fuerte (suma 20% extra de daño)
- Vida normal
- Defensa buena

### Mago
- Su ataque ignora la defensa del enemigo
- Ataque fuerte
- Defensa debil

### Arquero
- Si su ataque es mas fuerte que la defensa, hace el doble de daño (crítico)
- Si no, hace daño normal
- Defensa media

---

## Como funciona

Cada personaje tiene tres valores:
- Vida (va de 0 a 100)
- Ataque (cuanto daño hace)
- Defensa (cuanto daño reduce)

El juego hace esto:
1. Comienza la batalla con dos personajes
2. Por turnos, uno ataca al otro
3. Se calcula el daño segun el tipo de personaje
4. Se muestra cuanta vida le queda a cada uno
5. Cuando alguien llega a 0 de vida, se termina
6. Se dice quien gano

---

## Como correr el juego

Necesitas Python.

Ejecuta esto en la terminal:

```
python juego.py
```

---

## Ejemplo de crear tu propia batalla

```python
from batalla_limpia import Guerrero, Mago, Batalla

# Crear dos personajes
jugador1 = Guerrero(100, 30, 20)
jugador2 = Mago(80, 40, 10)

# Crear la batalla
batalla = Batalla(jugador1, jugador2)

# Empezar la batalla
batalla.iniciar()
```


## Las clases del codigo

El codigo tiene dos clases principales:

1. Personaje (clase base)
   - Tiene vida, ataque y defensa
   - Tiene un metodo atacar() que cada tipo usa diferente

2. Batalla (controla el juego)
   - Tiene dos personajes
   - Controla los turnos
   - Muestra el estado
   - Dice quien gano

Y tres clases que heredan de Personaje:
- Guerrero
- Mago
- Arquero

---

## Como se calcula el daño

Guerrero:
```
Daño = (Ataque x 1.20) - Defensa del otro
```

Mago:
```
Daño = Ataque (no importa la defensa)
```

Arquero:
```
Si Ataque > Defensa:
  Daño = (Ataque - Defensa) x 2

Si no:
  Daño = Ataque - Defensa
```
