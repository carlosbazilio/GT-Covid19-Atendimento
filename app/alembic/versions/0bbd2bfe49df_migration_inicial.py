"""Migration inicial

Revision ID: 0bbd2bfe49df
Revises: 
Create Date: 2020-08-24 17:18:30.555593

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0bbd2bfe49df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('atendimentos_iniciais',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('endereco', sa.String(length=255), nullable=True),
    sa.Column('qnt_comodos', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('is_agua_encanada', mysql.TINYINT(display_width=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beneficios_sociais',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cidades',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=60), nullable=False),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doencas_cronicas',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('etnias',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('generos',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('indicadores',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medicamentos',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('motivos_sair',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orientacoes_finais',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parentescos',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sintomas',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tentativas',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adms_saude',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('nome', sa.String(length=150), nullable=False),
    sa.Column('crm', sa.String(length=20), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.Column('perfil', sa.Enum('comum', 'admin', 'master'), nullable=True),
    sa.Column('senha', sa.String(length=150), nullable=False),
    sa.Column('id_cidade', mysql.INTEGER(display_width=11), nullable=True),
    sa.ForeignKeyConstraint(['id_cidade'], ['cidades.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_adms_saude_id_cidade'), 'adms_saude', ['id_cidade'], unique=False)
    op.create_table('estrategias_saude_familiar',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('value', sa.String(length=150), nullable=False),
    sa.Column('id_cidade', mysql.INTEGER(display_width=11), nullable=True),
    sa.ForeignKeyConstraint(['id_cidade'], ['cidades.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_estrategias_saude_familiar_id_cidade'), 'estrategias_saude_familiar', ['id_cidade'], unique=False)
    op.create_table('pacientes',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('nome', sa.String(length=150), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('cns', sa.String(length=15), nullable=True),
    sa.Column('telefone', sa.String(length=11), nullable=False),
    sa.Column('endereco', sa.String(length=255), nullable=False),
    sa.Column('data_nasc', sa.Date(), nullable=True),
    sa.Column('id_etnia', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('id_genero', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('id_cidade', mysql.INTEGER(display_width=11), nullable=True),
    sa.ForeignKeyConstraint(['id_cidade'], ['cidades.id'], ),
    sa.ForeignKeyConstraint(['id_etnia'], ['etnias.id'], ),
    sa.ForeignKeyConstraint(['id_genero'], ['generos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pacientes_id_cidade'), 'pacientes', ['id_cidade'], unique=False)
    op.create_index(op.f('ix_pacientes_id_etnia'), 'pacientes', ['id_etnia'], unique=False)
    op.create_index(op.f('ix_pacientes_id_genero'), 'pacientes', ['id_genero'], unique=False)
    op.create_table('tempos_contato_acompanhamento',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('intervalo_contato', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('tempo_maximo_acompanhamento', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('id_cidade', mysql.INTEGER(display_width=11), nullable=True),
    sa.ForeignKeyConstraint(['id_cidade'], ['cidades.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tempos_contato_acompanhamento_id_cidade'), 'tempos_contato_acompanhamento', ['id_cidade'], unique=False)
    op.create_table('atendimentos',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_atendimento_inicial', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('id_paciente', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('is_primeiro', mysql.TINYINT(display_width=4), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=False),
    sa.Column('fez_atendimento', mysql.TINYINT(display_width=1), nullable=True),
    sa.Column('id_tentativa', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('outras_tentativas', sa.String(length=255), nullable=True),
    sa.Column('cuidado_sair_casa', sa.String(length=255), nullable=True),
    sa.Column('consegue_isolamento', mysql.TINYINT(display_width=4), nullable=True),
    sa.Column('como_consegue', sa.String(length=255), nullable=True),
    sa.Column('porque_nao_consegue', sa.String(length=255), nullable=True),
    sa.Column('consegue_ficar_casa', mysql.TINYINT(display_width=4), nullable=True),
    sa.Column('quantos_dias', mysql.INTEGER(display_width=11), nullable=True),
    sa.ForeignKeyConstraint(['id_atendimento_inicial'], ['atendimentos_iniciais.id'], ),
    sa.ForeignKeyConstraint(['id_paciente'], ['pacientes.id'], ),
    sa.ForeignKeyConstraint(['id_tentativa'], ['tentativas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_atendimentos_id_atendimento_inicial'), 'atendimentos', ['id_atendimento_inicial'], unique=False)
    op.create_index(op.f('ix_atendimentos_id_paciente'), 'atendimentos', ['id_paciente'], unique=False)
    op.create_index(op.f('ix_atendimentos_id_tentativa'), 'atendimentos', ['id_tentativa'], unique=False)
    op.create_table('agendamentos',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_adm_saude', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_atendimento', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('id_paciente', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_adm_saude'], ['adms_saude.id'], ),
    sa.ForeignKeyConstraint(['id_atendimento'], ['atendimentos.id'], ),
    sa.ForeignKeyConstraint(['id_paciente'], ['pacientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_agendamentos_id_adm_saude'), 'agendamentos', ['id_adm_saude'], unique=False)
    op.create_index(op.f('ix_agendamentos_id_atendimento'), 'agendamentos', ['id_atendimento'], unique=False)
    op.create_index(op.f('ix_agendamentos_id_paciente'), 'agendamentos', ['id_paciente'], unique=False)
    op.create_table('atendimentos_beneficios_sociais',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_atendimento', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_beneficio_social', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('outros_beneficios_sociais', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['id_atendimento'], ['atendimentos.id'], ),
    sa.ForeignKeyConstraint(['id_beneficio_social'], ['beneficios_sociais.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_atendimentos_beneficios_sociais_id_atendimento'), 'atendimentos_beneficios_sociais', ['id_atendimento'], unique=False)
    op.create_index(op.f('ix_atendimentos_beneficios_sociais_id_beneficio_social'), 'atendimentos_beneficios_sociais', ['id_beneficio_social'], unique=False)
    op.create_table('atendimentos_estrategias_saudes_familiar',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_atendimento', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_estrategia_saude_familiar', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('outras_estrategias_saude_familiar', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['id_atendimento'], ['atendimentos.id'], ),
    sa.ForeignKeyConstraint(['id_estrategia_saude_familiar'], ['estrategias_saude_familiar.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_atendimentos_estrategias_saudes_familiar_id_atendimento'), 'atendimentos_estrategias_saudes_familiar', ['id_atendimento'], unique=False)
    op.create_index(op.f('ix_atendimentos_estrategias_saudes_familiar_id_estrategia_saude_familiar'), 'atendimentos_estrategias_saudes_familiar', ['id_estrategia_saude_familiar'], unique=False)
    op.create_table('atendimentos_motivos_sair',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_atendimento', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_motivo_sair', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('outros_motivos_sair', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['id_atendimento'], ['atendimentos.id'], ),
    sa.ForeignKeyConstraint(['id_motivo_sair'], ['motivos_sair.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_atendimentos_motivos_sair_id_atendimento'), 'atendimentos_motivos_sair', ['id_atendimento'], unique=False)
    op.create_index(op.f('ix_atendimentos_motivos_sair_id_motivo_sair'), 'atendimentos_motivos_sair', ['id_motivo_sair'], unique=False)
    op.create_table('atendimentos_orientacoes_finais',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_atendimento', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_orientacao_final', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('comentario', sa.String(length=255), nullable=True),
    sa.Column('outras_orientacoes_finais', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['id_atendimento'], ['atendimentos.id'], ),
    sa.ForeignKeyConstraint(['id_orientacao_final'], ['orientacoes_finais.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_atendimentos_orientacoes_finais_id_atendimento'), 'atendimentos_orientacoes_finais', ['id_atendimento'], unique=False)
    op.create_index(op.f('ix_atendimentos_orientacoes_finais_id_orientacao_final'), 'atendimentos_orientacoes_finais', ['id_orientacao_final'], unique=False)
    op.create_table('atendimentos_relacao',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_atendimento', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_sintoma', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('id_doenca_cronica', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('id_parentesco', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('id_indicador', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('medicamento', sa.String(length=150), nullable=True),
    sa.Column('dosagem', sa.String(length=150), nullable=True),
    sa.Column('data_sintomas', sa.DateTime(), nullable=True),
    sa.Column('is_mulher_gravida', mysql.TINYINT(display_width=4), nullable=True),
    sa.Column('outros_sintomas', sa.String(length=150), nullable=True),
    sa.Column('outras_doencas_cronicas', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['id_atendimento'], ['atendimentos.id'], ),
    sa.ForeignKeyConstraint(['id_doenca_cronica'], ['doencas_cronicas.id'], ),
    sa.ForeignKeyConstraint(['id_indicador'], ['indicadores.id'], ),
    sa.ForeignKeyConstraint(['id_parentesco'], ['parentescos.id'], ),
    sa.ForeignKeyConstraint(['id_sintoma'], ['sintomas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_atendimentos_relacao_id_atendimento'), 'atendimentos_relacao', ['id_atendimento'], unique=False)
    op.create_index(op.f('ix_atendimentos_relacao_id_doenca_cronica'), 'atendimentos_relacao', ['id_doenca_cronica'], unique=False)
    op.create_index(op.f('ix_atendimentos_relacao_id_indicador'), 'atendimentos_relacao', ['id_indicador'], unique=False)
    op.create_index(op.f('ix_atendimentos_relacao_id_parentesco'), 'atendimentos_relacao', ['id_parentesco'], unique=False)
    op.create_index(op.f('ix_atendimentos_relacao_id_sintoma'), 'atendimentos_relacao', ['id_sintoma'], unique=False)
    op.create_table('atendimentos_visitas',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_atendimento', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('quem_visitou', sa.String(length=150), nullable=True),
    sa.Column('porque_visitou', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['id_atendimento'], ['atendimentos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_atendimentos_visitas_id_atendimento'), 'atendimentos_visitas', ['id_atendimento'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('atendimentos_visitas')
    op.drop_table('atendimentos_relacao')
    op.drop_table('atendimentos_orientacoes_finais')
    op.drop_table('atendimentos_motivos_sair')
    op.drop_table('atendimentos_estrategias_saudes_familiar')
    op.drop_table('atendimentos_beneficios_sociais')
    op.drop_table('agendamentos')
    op.drop_table('atendimentos')
    op.drop_table('tempos_contato_acompanhamento')
    op.drop_table('pacientes')
    op.drop_table('estrategias_saude_familiar')
    op.drop_table('adms_saude')
    op.drop_table('tentativas')
    op.drop_table('sintomas')
    op.drop_table('parentescos')
    op.drop_table('orientacoes_finais')
    op.drop_table('motivos_sair')
    op.drop_table('medicamentos')
    op.drop_table('indicadores')
    op.drop_table('generos')
    op.drop_table('etnias')
    op.drop_table('doencas_cronicas')
    op.drop_table('cidades')
    op.drop_table('beneficios_sociais')
    op.drop_table('atendimentos_iniciais')
    # ### end Alembic commands ###