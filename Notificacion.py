class Notificacion:
    def enviar(self,mensaje):
        print("Notificacion base:",mensaje)

class NotificacionEmail(Notificacion):
    def enviar(self,mensaje):
        print("Enviando Email con el texto:",mensaje)

class NotificacionSMS(Notificacion):
    def enviar(self,mensaje):
        print("Enviando mensaje SMS al telefono:",mensaje)

class NotificacionPush(Notificacion):
    def enviar(self,mensaje):
        print("Enviando alerta Push a la app:",mensaje)

email=NotificacionEmail()
sms=NotificacionSMS()
push=NotificacionPush()


lista_notificaciones=[email,sms,push]

mensaje_urgente="El sistema se actualizara en 10 minutos"


for notificacion in lista_notificaciones:
    notificacion.enviar(mensaje_urgente)