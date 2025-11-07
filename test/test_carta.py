import pytest
from Clases.carta import Carta

@pytest.fixture
def carta():
    return Carta(5,'o')

def test_contructor(carta):
    assert carta.valor==5
    assert carta.palo=='o'
    assert carta.seleccionada==False

def test_mover(carta, monkeypatch):
    i,j=carta.x,carta.y
    llamado={}
    def mock_asignar_pos(x,y):
        llamado["x"]=x
        llamado["y"]=y
    monkeypatch.setattr(carta,"asignar_posicion",mock_asignar_pos)
    x_final,y_final=carta.x+10,carta.y+10
    carta.mover_hacia_destino()
    assert "x" in llamado and "y" in llamado
    assert llamado["x"]!=i