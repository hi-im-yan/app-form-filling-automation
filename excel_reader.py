import pandas as pd
from datetime import datetime, time

INPUT_DIRECTORY="./input_files/"

import pandas as pd

def load_rows(filename):
    df = pd.read_excel(INPUT_DIRECTORY + filename)
    return df.to_dict(orient="records")

def _format_date(value):
    if pd.isna(value):
        return ""

    if isinstance(value, (datetime, pd.Timestamp)):
        return value.strftime("%d/%m/%Y")

    return str(value)


def _format_time(value):
    if pd.isna(value):
        return ""

    if isinstance(value, time):
        return value.strftime("%H:%M")

    return str(value)


def _format_number(value):
    if pd.isna(value):
        return ""
    return str(value)


def map_row(row: dict) -> dict:
    return {
        # Serviço
        "service_type": str(row.get("Tipo de Serviço", "")),

        # Datas e horários
        "schedule_date": _format_date(row.get("DATA DE AGENDAMENTO")),
        "schedule_time": _format_time(row.get("HORA ATENDIMENTO")),
        "birth_date": _format_date(row.get("DATA DE NASCIMENTO")),

        # Estabelecimento / profissional
        "establishment": str(row.get("ESTABELECIMENTO", "")),
        "doctor_specialty": str(row.get("ESPECIALIDADE/MEDICO", "")),
        "doctor_cpf": _format_number(row.get("CPF DO MEDICO")),
        "doctor_cbo": _format_number(row.get("CBO DO MEDICO")),

        # Localidade
        "city": str(row.get("MUNICIPIOS", "")),
        "zone_type": str(row.get("TIPO_ZONA", "")),
        "address": str(row.get("ENDERECO_COMPLETO", "")),

        # Paciente
        "patient_name": str(row.get("PACIENTE", "")),
        "patient_cpf": str(row.get("CPF DO PACIENTE", "")),
        "patient_cns": str(row.get("CNS DO PACIENTE", "")),
        "patient_race": str(row.get("RACA DO PACIENTE", "")),
        "phone": str(row.get("TELEFONE", "")),

        # Consulta
        "cid": str(row.get("CID DA CONSULTA", "")),
    }
