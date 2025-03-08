class Usuario:
    nombredeusuario: str
    contraseña: str

    def __init__(self, nombredeusuario: str, contraseña: str):
        self.nombredeusuario = nombredeusuario
        self.contraseña = contraseña
    
    def iniciar_sesion(self, usuario: str, contraseña: str) -> str:
        if self.nombredeusuario == usuario and self.contraseña == contraseña:
            return f"Inicio de sesión exitoso para {self.nombredeusuario}"
        return "Error: Nombre de usuario o contraseña incorrectos."

class Administrador(Usuario):
    def __init__(self, nombredeusuario: str, contraseña: str):
        super().__init__(nombredeusuario, contraseña)
    
    def gestionar_usuarios(self) -> str:
        return "Gestionando usuarios..."

class Cliente(Usuario):
    def __init__(self, nombredeusuario: str, contraseña: str):
        super().__init__(nombredeusuario, contraseña)
    
    def realizar_compra(self) -> str:
        return "Realizando una compra..."


admin = Administrador("admin", "1234")
cliente = Cliente("cliente1", "abcd")


print(admin.iniciar_sesion("admin", "1234"))
print(admin.gestionar_usuarios())
print(cliente.iniciar_sesion("cliente1", "abcd"))
print(cliente.realizar_compra())
