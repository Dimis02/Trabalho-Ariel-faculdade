def calcular_novo_horario(hora_inicio, minuto_inicio, segundo_inicio, duracao_segundos):
    total_segundos = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio + duracao_segundos 
    hora_termino = total_segundos // 3600
    minuto_termino = (total_segundos % 3600) // 60
    segundo_termino = (total_segundos % 3600) % 60
    return hora_termino, minuto_termino, segundo_termino

def main():
    hora_inicio = int(input("Digite a hora de início da experiência: "))
    minuto_inicio = int(input("Digite o minuto de início da experiência: "))
    segundo_inicio = int(input("Digite o segundo de início da experiência: "))
    # Recebe a duração da experiência em segundos
    duracao_segundos = int(input("Digite a duração da experiência em segundos: "))
    
    hora_termino, minuto_termino, segundo_termino = calcular_novo_horario(hora_inicio, minuto_inicio, segundo_inicio, duracao_segundos)
    
    print("Horário de término da experiência:", hora_termino, "horas,", minuto_termino, "minutos e", segundo_termino, "segundos.")

if __name__ == "__main__":
    main()
