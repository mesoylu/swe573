var field_index = 1;

function subscribe(communityName) {
    var rf = function (res) {
        location.reload();
    };
    var url = 'members/';
    var data = {
        name: communityName
    }
    $.post(url, data, rf);
}

function unsubscribe(communityName) {
    var url = 'members/';
    $.ajax({
        url: url,
        type: 'DELETE',
        success: function (result) {
            location.reload();
        }
    });
}

function addDataFieldRow() {
    var rf = function (res) {
        $('#has_fields').val(field_index);
        var button = $('#button_row');
        $(res).insertBefore(button);
        field_index++;
    };
    var url = '/fieldform';
    var data = {
        index: field_index
    }
    $.post(url, data, rf);
}

function submitDataType() {
    // var form = $('#create_datatype');
    // var rf = function (res) {
    //     location.reload();
    // };
    // var url = '../datatypes/';
    // var data = {
    //     formdata: form.serialize()
    // }
    // $.post(url, data, rf);
    var json = {};
    json.name = '1';
    json.description = '2';
    var rf = function (res) {
        location.reload();
    };
    var url = '../datatypes/';
    var data = json;
    $.post(url, data, rf);
}

function enableEnumeration(e){
    if(e.value == 'enumeration'){
        var id = $(e).attr('data-id');
        var elementId = '#enum_' + id;
        $(elementId).show();
    } else {
        var id = $(e).attr('data-id');
        var elementId = '#enum_' + id;
        $(elementId).hide();
    }
}

function getDataFields(e){
    var id = e.value
    var element = 'dt_' + id;
    console.log(element);
    var value = JSON.parse(document.getElementById(element).textContent);
    console.log(value);
    // var rf = function (res) {
    //     $('#has_fields').val(field_index);
    //     var button = $('#button_row');
    //     $(res).insertBefore(button);
    //     field_index++;
    // };
    // var url = '/fieldform';
    // var data = {
    //     index: field_index
    // }
    // $.post(url, data, rf);
}