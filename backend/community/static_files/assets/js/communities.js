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

