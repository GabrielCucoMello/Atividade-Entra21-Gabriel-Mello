from src.database_connect import chuva_hoje

funcionarios_normal = 90

if chuva_hoje >= 24:
    funcionarios_final = funcionarios_normal * 0.40
elif chuva_hoje == 23:
    funcionarios_final = funcionarios_normal * 0.45
elif chuva_hoje == 22:
    funcionarios_final = funcionarios_normal * 0.50
elif chuva_hoje == 21:
    funcionarios_final = funcionarios_normal * 0.55
elif chuva_hoje == 20:
    funcionarios_final = funcionarios_normal * 0.60
elif chuva_hoje >= 16:
    funcionarios_final = funcionarios_normal * 0.65
elif chuva_hoje >= 14:
    funcionarios_final = funcionarios_normal * 0.7
elif chuva_hoje >= 13:
    funcionarios_final = funcionarios_normal * 0.8
elif chuva_hoje >= 8:
    funcionarios_final = funcionarios_normal * 0.9
elif chuva_hoje <= 7:
    funcionarios_final = funcionarios_normal