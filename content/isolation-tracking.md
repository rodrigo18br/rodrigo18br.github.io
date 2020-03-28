Title: Acompanhando o isolamento em resposta ao COVID-19 através de redes sociais
Date: 2020-03-25
Tags: data-science, instagram
Description: O que posts no Instagram podem nos contar sobre isolamento populacional em época de pandemia?
Authors: Rodrigo Oliveira

O cenário recente da pandemia de COVID-19 traz o risco de que com um grande número de casos simultâneos haja um colapso no sistema de saúde, com escassez de leitos e recursos. A fim de desacelerar o contágio, especialistas passaram a recomendar o isolamento social de grande parte da população, de modo a evitar aglomerações em que a contaminação é fácil de acontecer. Com a chegada do vírus no Brasil, diversos governos a nível estadual e municipal passaram a determinar o fechamento de estabelecimentos públicos para estimular o isolamento.

Isso leva à pergunta: de que modo é possível identficar se está realmente acontecendo isolamento num nível que diminua o ritmo de contágio? Visto que uma grande quantidade de pessoas registra suas atividades em rede sociais, é de se esperar que caso elas estejam de fato se isolando, uma mudança nos padrões de seus conteúdos aparecerá.

Neste artigo irei realizar uma análise de posts no Instagram para identificar se houve alguma mudança nos posts situados em locais externos com a chegada do COVID-19 no Brasil. Antes de partir para os aspectos técnicos, é necessário ter em mente algumas limitações do que será feito aqui:

* Apenas uma parcela da população utiliza o Instagram, logo o conteúdo extraído dele será parcialmente generalizável. Certas demografias, como idosos, possuem baixa presença na rede social e seu comportamento não será bem detectável a partir dela;

* Usuários certas vezes postam conteúdos que foram produzidos em momentos anteriores, portanto a atividade no Instagram num período de tempo não necessariamente reflete as atividades reais dos usuários;

* Este artigo não é um estudo científico completo, que demandaria mais tempo e validação. O que fiz aqui tem o fim de ser apenas um protótipo de como a tarefa pode ser realizada.

### Dados a coletar

O primeiro caso de COVID-19 foi confirmado no Brasil em 25 de fevereiro. Apesar de já haver preocupações com o vírus anteriormente, foi a partir desse momento em que medidas começaram a ser tomadas ao longo do país. Como foco tomarei a minha cidade natal, Feira de Santana, onde foi confirmado o primeiro caso na Bahia, em 6 de março. É necessário saber o comportamento dos usuários por um tempo antes da chegada do COVID-19, para estabelecer se houve uma mudança real. Agrupei os dados obtidos pela semana anual em que foram publicados. Os resultados vão da semana 4 (iniciada em 25 de janeiro) até a semana 12 (terminada em 22 de março) desse ano.

Ao longo do mês de março, medidas foram sendo tomadas pela prefeitura para conter o fluxo de pessoas. No [dia 16](http://www.feiradesantana.ba.gov.br/servicos.asp?titulo=Prefeito%20suspende%20aulas%20em%20escolas%20e%20faculdades%20por%2015%20dias,%20al%C3%A9m%20de%20outras%20medidas%20restritivas%20em%20preven%C3%A7%C3%A3o%20ao%20Coronav%C3%ADrus&id=7&link=secom/noticias.asp&idn=24346#noticias), aulas em escolas e universidades foram suspensas por 15 dias, no [dia 18](http://www.feiradesantana.ba.gov.br/servicos.asp?titulo=Shoppings%20funcionar%C3%A3o%20em%20hor%C3%A1rio%20reduzido&id=1&link=secom/noticias.asp&idn=24359#noticias) o horário de funcionamento de Shopping Centers foi reduzido, e o comércio foi fechado totalmente (com exceção de supermercados e farmácias) [no dia 21](http://www.feiradesantana.ba.gov.br/servicos.asp?titulo=Fiscaliza%C3%A7%C3%A3o%20Preventiva%20Integrada%20fecha%20lojas,%20no%20com%C3%A9rcio%20de%20Feira,%20que%20abriram%20neste%20s%C3%A1bado%20&id=9&link=secom/noticias.asp&idn=24387#noticias). Estas datas se situam na 12º semana do ano. Existem, assim, duas questões a serem levantadas:

1. A partir da divulgação dos primeiros casos, no início de março, existiu alguma mudança nos hábitos nos usuários em seus posts marcados em localidades externas?
2. A partir das medidas oficiais determinando suspensões de atividades de diversos estabelecimentos, houve uma redução de posts marcados nestes locais?

### Coletando dados

Existem diversas bibliotecas para acessar os endpoints do Instagram. Utilizei a [Instagram-API](https://github.com/mgp25/Instagram-API), que apesar de ter recebido um DMCA do Facebook [ref]Cf. https://news.ycombinator.com/item?id=22209892 para uma discussão sobre.[/ref], possui forks [ref]https://gitlab.com/alihesari/Instagram-API[/ref] [ref]https://github.com/NantipatSoftEn/Instagram-API[/ref] e está disponível para instalação via Composer [ref]https://packagist.org/packages/mgp25/instagram-php[/ref] [ref]Também existe um [port](https://github.com/LevPasha/Instagram-API-python) da API para Python, que contudo não tem todos os endpoints implementados.[/ref]. É possível fazer uma busca por locais no Instagram fornecendo uma latitude e longitude. Essa busca traz os seguintes resultados:

1. Locais geográficos como a própria cidade e os bairros e ruas próximos. Visto que pessoas podem postar fotos dentro de suas casas e marcá-las nesses locais, essas localizações foram ignoradas;
2. Locais "de brincadeira" que são marcados para fins de piada, que também foram ignoradas;
3. Estabelecimentos públicos como restaurantes, escolas, bares, shoppings etc.

Deste último grupo de resultados foram extraídos todos os posts até alcançar a 4º semana do ano. Esses posts foram contados por semana. Iniciei com localidades próximas da Avenida Getúlio Vargas, uma das principais do centro da cidade. Com a baixa quantidade de locais com dados aproveitáveis (como explico na próxima seção), decidi procurar por alguns locais que presumi que seriam mais frutíferos:

* A principal universidade da cidade, Universidade Estadual de Feira de Santana;

* Dois shoppings da cidade, o Boulevard Shopping e o América Outlet.

### Resultados

Certos locais possuíam um número muito pequeno de posts associados, o que impossibitava uma análise adequada. Me limitei a locais que possuíssem pelo menos mais de 10 resultados em pelo menos uma semana.

Os primeiros resultados que saltam aos olhos são os de universidades, que fazem parte do primeiro grupo de estabelecimentos fechados pela prefeitura. Em primeiro lugar, considerando que as aulas começaram no início de fevereiro, é fácil entender o súbito aumento no número de posts por volta da semana 6. A semana 9, em que ocorreu o carnaval e o recesso associado, possui uma queda significativa em posts. Assim, existe associação entre inatividade nesses locais e o número de postagens.

![Resultados para Universidade Estadual de Feira de Santana]({static}/img/uefs.png)
![Resultados para Faculdade Anísio Teixeira]({static}/img/fat.png)
![Resultados para Universidade Salvador]({static}/img/unifacs.png)

No que diz respeito às reações ao COVID-19, só aconteceu uma queda indicativa de isolamento na semana 12, que coincide com o início da suspensão de todos os estabelecimentos de ensino. Assim, nota-se que o anúncio dos primeiros casos na cidade não causou mudança nos hábitos até que o governo tomasse uma medida.

Os resultados seguintes são de um espaço de festas voltado para casamentos. Não existe nenhuma diferença signficativa na quantidade de posts após a descoberta dos primeiros casos, mesmo se tratando de um lugar de aglomerações costumeiras.

![Resultados para Mansão Soláris]({static}/img/solaris.png)

Os resultados no Shopping Boulevard e no Shopping América Outlet só mostraram uma queda significativa na atividade quando se iniciou a restrição de horário de funcionamento. No caso do Shopping Boulevard, foram feitos mais de 100 posts, quantidade ainda bastante alta, indicando que aglomerações ainda estavam potencialmente acontecendo.

![Resultados para Shopping Boulevard]({static}/img/boulevard.png)
![Resultados para América Outlet]({static}/img/outlet.png)

### Conclusões e perspectivas futuras

Os dados mostrados aqui indicam que os posts de Instagram marcados em localidades públicas exibiram redução significativa apenas no período de tempo em que essas localidades estavam sob restrições de funcionamento pelas autoridades. Se essas quantidades refletem o fluxo de pessoas em locais públicos, isso significa que nas primeiras semanas posteriores aos primeiros diagnósticos do COVID-19.

Essa análise pode ser expandida de diversos modos. Através de Machine Learning, as fotos postadas podem ser analisadas para identificar as que foram tiradas em locais externos. Assim, os posts analisados não estariam limitados aos que foram explicitamente marcados em localidades. Outra extensão está na análise não apenas de posts permanentes, mas de stories, que pelo visto são mais publicados com maior frequência. Contudo, como um story só dura 24 horas, é necessário monitorá-los e registrar as publicações que sejam relevantes.

