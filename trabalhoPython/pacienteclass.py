
class paciente:
    def __init__(self, nome, exame, data, hora):
        self._nome = nome
        self._exame = exame
        self._data = data
        self._hora = hora

    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get_cod(self):
        return self._cod
    def _set_cod(self, cod):
        self._cod = cod
    def _get_exame(self):
        return self._exame
    def _set_exame(self, exame):
        self._exame = exame
    def _get_data(self):
        return self._data
    def _set_data(self, data):
        self._data = data
    def _get_hora(self):
        return self._hora
    def _set_hora(self, hora):
        self._hora = hora
    nome = property( _get_nome, _set_nome)
    exame = property( _get_exame, _set_exame)
    data = property( _get_data, _set_data)
    hora = property( _get_hora, _set_hora)
    cod = property( _get_cod, _set_cod)

p = paciente('Julio','consulta','10/10/2019','12:10')
print (p.nome)
