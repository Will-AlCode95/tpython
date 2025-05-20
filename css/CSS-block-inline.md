# CSS - Layout - Block e Inline

Tudo que estilamos com CSS está dentro de uma caixa. Para o CSS, o documento HTML é como uma composição de caixas, dentro de caixas, dentro caixas... desde o corpo da página até o conteúdo dos elementos.

![caixas dentro de caixas](/img/boxes.jpg)

O modo como as caixas serão dispostas na página depende de seu **modo de exibição**, controlado pela propriedade <code>display</code> do elemento.

Os dois modos de exibição que usamos até agora foram os modos padrão:

- <code>inline</code> - ex. span, que é um elemento inline
- <code>block</code> - ex. div, que é um elemento block

![](/img/inline-block.jpg)

## Mostrando e escondendo caixas

Podemos retirar uma caixa da página sem apagar seu conteúdo. Para isso alteramos o valor da propriedade **display** para "none". 

Além da propriedade **display** existe a **visibility**, que pode ter valor **hidden**. 

A diferença é que <code>display: none;</code> retira a caixa do meio das caixas que são exibidas, alterando a disposição das caixas na página. Já <code>visibility: hidden</code> mantém a caixa no lugar, inclusive o espaço ocupado por ela na página, e apenas esconde seu conteúdo.

## Dimensionamento e conteúdo

O tamanho das caixas pode ser alterado explicitamente com CSS (dimensionamento extrínseco) usando propriedades como <code>width/height</code> ou pelo browser, de acordo com o conteúdo das caixas,  (dimensionamento intrínseco) se deixarmos as propriedades <code>width/height</code> sem valor ou se usarmos valores variáveis predefinidos, como <code>min-content</code>.

## display block/inline

Elementos com propriedade **display** = *inline* não podem ter **width** e **height** manipulados explicitamente pelo CSS. 

Elementos com propriedade **display** = *block* criam uma linha para si e por padrão tem largura igual ao tamanho da linha onde estão e suas margens são respeitadas pelos elementos ao redor deles.