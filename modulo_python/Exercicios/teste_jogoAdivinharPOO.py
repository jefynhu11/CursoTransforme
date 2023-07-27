from jogoAdivinharPOOTeste import JogoAdivinhar
import pytest

@pytest.fixture
def jogo():
    return JogoAdivinhar('jef', 1, 100, 5);

def test_constructor(jogo):
    assert jogo.inferior == 1;
    assert jogo.superior == 100;
    assert jogo.maxTentativa == 5;