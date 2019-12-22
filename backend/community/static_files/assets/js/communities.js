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

function deleteDataFieldRow(e){
    var index = $(e).attr('data-id');
    var df_name = '#data_field_' + index;
    var choice_name = '#choice_' + index;
    $(df_name).remove();
    $(choice_name).remove();
    field_index--;
    // todo should rearrange indexes if a user deletes a datafield other than the last one
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

function enableChoices(e){
    if(e.value == 'enumeration' || e.value == 'multiple'){
        var id = $(e).attr('data-id');
        var elementId = '#choice_' + id;
        $(elementId).show();
    } else {
        var id = $(e).attr('data-id');
        var elementId = '#choice_' + id;
        $(elementId).hide();
    }
}

function getDataFields(e){
    $('.data_field').remove();
    var id = e.value
    if(id>0) {
        var rf = function (res) {
            var button = $('#button_row');
            $(res).insertBefore(button);
        };
        var url = '/postfieldsform';
        var data = {
            index: id
        }
        $.post(url, data, rf);
    }
}

function addListItem(e){
    var parent = $(e).parent().parent();
    var clone = parent.clone();
    clone.children().eq(1).children().eq(0).val("");
    clone.insertAfter(parent);
    console.log(clone);
}

function removeListItem(e){
    var parent = $(e).parent().parent();
    parent.remove();
}
