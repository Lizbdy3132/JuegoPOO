from abc import ABC, abstractmethod


class Personaje(ABC):
    
    def __init__(self, vida, ataque, defensa):
        self._vida = 0
        self._ataque = ataque
        self._defensa = defensa
        self.vida = vida

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        elif valor > 100:
            self._vida = 100
        else:
            self._vida = valor

    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, valor):
        if valor < 0:
            self._ataque = 0
        else:
            self._ataque = valor

    @property
    def defensa(self):
        return self._defensa

    @defensa.setter
    def defensa(self, valor):
        if valor < 0:
            self._defensa = 0
        else:
            self._defensa = valor

    @abstractmethod
    def atacar(self, objetivo):
        pass

    def esta_vivo(self):
        return self._vida > 0


class Guerrero(Personaje):
    
    def atacar(self, objetivo):
        dano_potencial = self.ataque * 1.20
        dano_final = max(0, dano_potencial - objetivo.defensa)
        
        nueva_vida = objetivo.vida - dano_final
        objetivo.vida = nueva_vida
        
        print(f"⚔️ Guerrero golpea fuerte a {objetivo.__class__.__name__}!")
        print(f"   Cálculo: ({self.ataque} × 1.20) - {objetivo.defensa} = {dano_final:.2f} de daño")
        print(f"   Causa {dano_final:.2f} de daño.")


class Mago(Personaje):
    
    def atacar(self, objetivo):
        dano_final = self.ataque
        
        nueva_vida = objetivo.vida - dano_final
        objetivo.vida = nueva_vida
        
        print(f"🔮 Mago lanza un hechizo que ignora la defensa!")
        print(f"   Cálculo: {self.ataque} de daño mágico (ignora {objetivo.defensa} de defensa)")
        print(f"   Causa {dano_final} de daño mágico.")


class Arquero(Personaje):
    
    def atacar(self, objetivo):
        base_ataque = self.ataque
        defensa_rival = objetivo.defensa
        
        if base_ataque > defensa_rival:
            dano_final = (base_ataque - defensa_rival) * 2
            print(f"🏹 Arquero acertó un tiro crítico!")
            print(f"   Cálculo: ({base_ataque} - {defensa_rival}) × 2 = {dano_final} de daño")
        else:
            dano_final = max(0, base_ataque - defensa_rival)
            print(f"🏹 Arquero disparó una flecha.")
            print(f"   Cálculo: {base_ataque} - {defensa_rival} = {dano_final} de daño")

        nueva_vida = objetivo.vida - dano_final
        objetivo.vida = nueva_vida
        print(f"   Causa {dano_final} de daño.")


class Batalla:
    
    def __init__(self, personaje1, personaje2):
        self._personaje1 = personaje1
        self._personaje2 = personaje2
        self._turno = 0

    @property
    def personaje1(self):
        return self._personaje1

    @personaje1.setter
    def personaje1(self, valor):
        self._personaje1 = valor

    @property
    def personaje2(self):
        return self._personaje2

    @personaje2.setter
    def personaje2(self, valor):
        self._personaje2 = valor

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        if valor < 0:
            self._turno = 0
        else:
            self._turno = valor

    def iniciar(self):
        print(f"\n{'='*60}")
        print(f"🏰 COMIENZA LA BATALLA 🏰")
        print(f"{'='*60}\n")
        self.mostrar_estado()
        
        while self._personaje1.esta_vivo() and self._personaje2.esta_vivo():
            self._turno += 1
            print(f"\n--- Turno {self._turno} ---")
            
            self._personaje1.atacar(self._personaje2)
            self.mostrar_estado()
            
            if not self._personaje2.esta_vivo():
                print(f"\n💀 {self._personaje2.__class__.__name__} ha sido derrotado...\n")
                break
            
            self._personaje2.atacar(self._personaje1)
            self.mostrar_estado()
            
            if not self._personaje1.esta_vivo():
                print(f"\n💀 {self._personaje1.__class__.__name__} ha sido derrotado...\n")
                break

        print(f"{'='*60}")
        print("--- Fin del juego ---")
        self._mostrar_ganador()
        print(f"{'='*60}\n")

    def mostrar_estado(self):
        p1_tipo = self._personaje1.__class__.__name__
        p2_tipo = self._personaje2.__class__.__name__
        
        print(f"\n Estado:")
        print(f"   {p1_tipo}: {self._personaje1.vida:.2f} HP | Ataque: {self._personaje1.ataque} | Defensa: {self._personaje1.defensa}")
        print(f"   {p2_tipo}: {self._personaje2.vida:.2f} HP | Ataque: {self._personaje2.ataque} | Defensa: {self._personaje2.defensa}")

    def hay_ganador(self):
        return not (self._personaje1.esta_vivo() and self._personaje2.esta_vivo())

    def _mostrar_ganador(self):
        if self._personaje1.esta_vivo():
            ganador = self._personaje1.__class__.__name__
        else:
            ganador = self._personaje2.__class__.__name__
        
        print(f"🏆 ¡El ganador es: {ganador}! 🏆")


if __name__ == "__main__":
    arturo = Guerrero(100, 30, 20)
    merlin = Mago(80, 40, 10)
    
    batalla = Batalla(arturo, merlin)
    
    batalla.iniciar()