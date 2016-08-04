*************************************
metodista.site.portlets
*************************************

.. contents:: Conteúdo
   :depth: 2

Introdução
----------

Produto com funcionalidades de portlets para portais.

Portlets
-----------------

Portlets
^^^^^^^^

Estado do pacote
----------------

O produto **metodista.site.portlets** possui testes automatizados e cobertura de testes pelos serviços Travis e CoverAlls.

Segue abaixo imagens com estado atual do branch master dos testes e cobertura deste produto:

.. image:: https://travis-ci.org/MetodistaWeb/metodista.site.portlets.svg?branch=master
   :target: https://travis-ci.org/MetodistaWeb/metodista.site.portlets

.. image:: https://coveralls.io/repos/github/MetodistaWeb/metodista.site.portlets/badge.svg
   :target: https://coveralls.io/github/MetodistaWeb/metodista.site.portlets


Instalação
----------

Para habilitar a instalação deste produto em um ambiente que utilize o
buildout:

1. Editar o arquivo buildout.cfg (ou outro arquivo de configuração) e
   adicionar o pacote ``metodista.site.portlets`` à lista de eggs da instalação::

        [buildout]
        ...
        eggs =
            metodista.site.portlets

2. Após alterar o arquivo de configuração é necessário executar
   ''bin/buildout'', que atualizará sua instalação.

3. Reinicie o Plone

4. Instale o produto
