import ast

def python_para_plantuml(codigo_python):
    '''
    Converte um código Python simples, contendo classes, em código PlantUML.
    '''
    arvore = ast.parse(codigo_python, type_comments=False)

    classes = []
    herancas = []

    for no in arvore.body:
        if isinstance(no, ast.ClassDef):
            nome_classe = no.name
            atributos = set()
            metodos = []

            for base in no.bases:
                if isinstance(base, ast.Name):
                    herancas.append((base.id, nome_classe))

            for item in no.body:
                if isinstance(item, ast.FunctionDef):
                    metodos.append(item.name)

                    for sub_no in ast.walk(item):
                        if (
                            isinstance(sub_no, ast.Attribute)
                            and isinstance(sub_no.value, ast.Name)
                            and sub_no.value.id == "self"
                        ):
                            atributos.add(sub_no.attr)

            classes.append({
                "nome": nome_classe,
                "atributos": sorted(atributos),
                "metodos": metodos
            })

    linhas = []
    linhas.append("@startuml")
    linhas.append("")
    linhas.append("title Diagrama gerado a partir de código Python")
    linhas.append("")

    for classe in classes:
        linhas.append(f"class {classe['nome']} {{")
        for atributo in classe["atributos"]:
            linhas.append(f"    - {atributo}")
        if classe["atributos"] and classe["metodos"]:
            linhas.append("")
        for metodo in classe["metodos"]:
            linhas.append(f"    + {metodo}()")
        linhas.append("}")
        linhas.append("")

    for classe_pai, classe_filha in herancas:
        linhas.append(f"{classe_pai} <|-- {classe_filha}")

    linhas.append("")
    linhas.append("@enduml")

    return "\n".join(linhas)

def gerar_arquivo_puml(nome_arquivo, codigo_python):
    '''
    Gera um arquivo .puml a partir de código Python para ser lido no VS Code.
    '''
    codigo_uml = python_para_plantuml(codigo_python)

    print("=== Código PlantUML gerado ===")
    print(codigo_uml)

    # Cria e salva o arquivo com a extensão .puml
    nome_completo = f"{nome_arquivo}.puml"
    with open(nome_completo, "w", encoding="utf-8") as arquivo:
        arquivo.write(codigo_uml)
    
    print(f"\n Arquivo '{nome_completo}' salvo com sucesso!")

# ==========================================
# TESTANDO O CÓDIGO
# ==========================================

meu_codigo_python = """
def __init__(self, nome, matricula, curso):
    self.nome = nome
    self.matricula = matricula
    self.curso = curso

def mostrar_informacoes(self):
    print(f"Aluno: {self.nome}")
    print(f"Matrícula: {self.matricula}")
    print(f"Curso: {self.curso}")
"""

# Executa a função passando o nome do arquivo que queremos gerar e o código
gerar_arquivo_puml("diagrama_veiculos", meu_codigo_python)