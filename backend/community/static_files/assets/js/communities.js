function subscribe(communityName) {
    var rf = function (res) {
        console.log('elelelele');
    };
    var url = communityName + '/members/';
    var data = {
        name : communityName
    }
    $.post(url,data,rf);
}

function unsubscribe(communityName) {
    var url = communityName + '/members/';
    $.ajax({
    url: url,
    type: 'DELETE',
    success: function(result) {
        console.log('lalalala');
    }
});
}