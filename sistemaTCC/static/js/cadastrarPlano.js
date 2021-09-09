function data_dia_inicio() {
    var tipo = document.getElementById("tipo");
    var max = tipo.value;
    var min = parseInt(document.getElementById('posicao').value);
    var select = document.getElementById('select');
    tipo.addEventListener("change", function () {
        max = parseInt(document.getElementById("tipo").value);
        limparOption(select)
        criarOption(min,max,select);
        data_dia_final(min,max)
    });
    limparOption(select);
    criarOption(min, max,select);

    select.addEventListener("change", function () {
        data_dia_final(min,max);
    });
}

function data_dia_final(min,max) {
    var select2 = document.getElementById('select2');
    limparOption(select2);
    min += 1
    criarOption(min,max,select2)
}

function limparOption(select) {
    var length = select.options.length;
    for (i = length - 1; i >= 0; i--) {
        select.options[i] = null;
    }
    var a = document.createElement('option');
    a.value = "";
    a.innerHTML = "Escolha um dia";
    select.appendChild(a);

}

function criarOption(min, max, select) {
    for (var i = min; i <= max; i++) {
        var opt = document.createElement('option');
        opt.setAttribute("id", i);
        opt.value = i;
        opt.innerHTML = i;
        select.appendChild(opt);
    }
}

var btn = document.getElementById("btn");
btn.addEventListener("click", function () {

    var select1 = document.getElementById("select").value;
    var select2 = document.getElementById("select2").value;
    var quantidade = document.getElementById("quantidade").value;
    var texto = document.getElementById("json");
    if (texto.value == "") {
        texto.value = texto.value + '{"dias": [' + select1 + ', ' + select2 + '],"quantidade": ' + quantidade + '}';
    } else {
        texto.value = texto.value + ',{"dias": [' + select1 + ', ' + select2 + '],"quantidade": ' + quantidade + '}'
    }

    var tbodyRef = document.getElementById('myTable').getElementsByTagName('tbody')[0];

    var newRow = tbodyRef.insertRow();
    var newCell = newRow.insertCell();
    var newCell2 = newRow.insertCell();

    var dias = document.createTextNode("Do " + select1 + "º  até " + select2 + "º dia");
    var quantidade = document.createTextNode(quantidade + " gramas");

    newCell.appendChild(dias);
    newCell2.appendChild(quantidade);
    newRow.appendChild("Adicionar periodo")

    quantidade = "";
    max = 114;
    min = parseInt(select2) + 1;

    document.getElementById('posicao').value = min;
    data_dia_inicio();
    limparOption(document.getElementById("select2"));
});

var btnCadastrar = document.getElementById("cadastrarPlano");

btnCadastrar.addEventListener("click", function () {
    var nome = document.getElementById("nome");
    var descricao = document.getElementById("descricao");

    if (nome.value == "") {
        alert("Preencha o campo nome do plano!");

        return false;
    }
    if (descricao.value == "") {
        alert("Preencha o campo descrição do plano!");
        return false;
    }
});