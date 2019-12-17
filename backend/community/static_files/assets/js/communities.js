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
    var form = $('#create_datatype');
    console.log(form.serialize());
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