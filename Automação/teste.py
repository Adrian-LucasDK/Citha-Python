from plyer import notification

def lembrete():
    notification.notify(
        title="Beba água",
        message="Não esqueça!",
        timeout=10  # Tempo de exibição da notificação (segundos)
    )

lembrete()
