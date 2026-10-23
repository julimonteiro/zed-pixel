// Pixel Arcade: cada nivel deve receber uma cor diferente.
const camadas = ((([ [{ itens: [1, 2, { valor: (3 + (4 * 5)) }] }] ])));

function inventario(jogador) {
  return {
    nome: "Pixel Arcade",
    itens: [
      { nome: "Espada", atributos: { ataque: 16, bonus: [2, 4, 8] } },
      { nome: "Pocao", atributos: { cura: 32, bonus: [1, 3, 5] } },
    ],
    ativo: true,
  };
}
