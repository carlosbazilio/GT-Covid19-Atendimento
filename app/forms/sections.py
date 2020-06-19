from .inputs import *

doencasCronicas = {
    "name": "Doenças Crônicas",
    "inputs": [
        doencaCronica,
    ]
}

medicamentos = {
    "name": "Medicamentos",
    "inputs": [
        checkRemedioPaciente
    ]
}

esfReferencia = {
    "name": "ESF de Referência",
    "inputs": [
        esf
    ]
}

informacoesBasicas = {
    "name": "Informações Básicas do Paciente",
    "inputs": [
        nome,
        cpf,
        telefone,
        aniversario,
        sexo,
        raca,
        endereco
    ]
}

condicaoclinica = {
    "name": "Comorbidades",
    "inputs": [
        comorbidades,
        dataPrimeiroSintoma,
    ]
}

domicilio = {
    "name": "Domicílio",
    "inputs": [
        moraSozinho
    ]
}

caracteristicasDomicilioAuxilio = {
    "name": "Características do domicílio e auxílios governamentais",
    "inputs": [
        qntComodos,
        aguaEncanada,
        recebeAuxilio
    ]
}

isolamentoDomiciliar = {
    "name": "Isolamento Domiciliar",
    "inputs": [
        consegueIsolamentoDomiciliar,
        consegueManterQuarentena
    ]
}

visitas = {
    "name": "Visitas",
    "inputs": [
        recebeuVisita,
    ]
}

sintomascovid = {
    "name": "Perguntas sobre os sintomas da Covid-19",
    "inputs": [
        apresentouSintomasCovid19,
        apresentouFebreQuantosGraus,
        tomouAlgumMedicamentoProsSintomas,
        alguemMaisApresentaSintomaEmCasa
    ]
}

orientacoesfinais = {
    "name": "Encerramento do atendimento/Orientações finais",
    "inputs": [
        orientacaoFinal,
        anotarOrientacoes
    ]
}
