$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const src = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes
        if(content){
            list = content.split(",")
            list[0] = list[0].replace("[","")
            list[1] = list[1].replaceAll("'","")
            list[2] = list[2].replaceAll("'","")
            list[3] = list[3].replaceAll("'","")
            list[3] = list[3].replace("]","")
        }


        
        const modal = $(this)

        if (src === 'New Case') {
            modal.find('.modal-title').text(src)
            //$('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Case ' + list[0])
        }
        if (content) {
            modal.find('.form-control1').val(list[0]);
            modal.find('.form-control2').val(list[1]);
            modal.find('.form-control3').val(list[2]);
            modal.find('.form-control4').val(list[3]);

        } else {
            modal.find('.form-control1').val('');
            modal.find('.form-control2').val('');
            modal.find('.form-control3').val('');
            modal.find('.form-control4').val('');
        }
    })

    $('#search-modal').on('show.bs.modal', function() {

    })

    $('#add-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const src = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes
        if(content){
            list = content.split(",")
            list[0] = list[0].replace("[","")
            list[1] = list[1].replaceAll("'","")
            list[2] = list[2].replaceAll("'","")
            list[3] = list[3].replaceAll("'","")
            list[3] = list[3].replace("]","")
        }


        
        const modal = $(this)
        modal.find('.modal-title').text('New Case')
    })


    $('#submit-task-edit').click(function () {
        // const tID = $('#task-form-display').attr('taskID');

        const caseNum = parseInt($('#task-modal').find('.form-control1').val())
        const Date = $('#task-modal').find('.form-control2').val()
        const Time = $('#task-modal').find('.form-control3').val()
        const Location = $('#task-modal').find('.form-control4').val()
        console.log(caseNum,Date,Time,Location)

        $.ajax({
            type: 'POST',
            url: '/edit/' + caseNum ,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [caseNum,Date,Time,Location]
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#back-home').click(function () { 
        location.assign('index.html');
    })

    $('#submit-task-add').click(function () {
        // const tID = $('#task-form-display').attr('taskID');


        const eventCaseNum = parseInt($('#add-modal').find('.form-control1').val())
        const reportDate = $('#add-modal').find('.form-control2').val()
        const eventDate = $('#add-modal').find('.form-control3').val()
        const eventTime = $('#add-modal').find('.form-control4').val()
        const eventLocation = $('#add-modal').find('.form-control5').val()
        const latitude = $('#add-modal').find('.form-control6').val()
        const longitude = $('#add-modal').find('.form-control7').val()
        const crimeCode = parseInt($('#add-modal').find('.form-control8').val())
        const weaponCode = $('#add-modal').find('.form-control9').val()
        const areaCode = $('#add-modal').find('.form-control10').val()
        const premiseCode = $('#add-modal').find('.form-control11').val()

        console.log(eventCaseNum,reportDate,eventDate,eventTime,eventLocation,latitude,longitude,crimeCode,weaponCode,areaCode,premiseCode)

        
        $.ajax({
            type: 'POST',
            url:  '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [eventCaseNum,reportDate,eventDate,eventTime,eventLocation,"",latitude,longitude,crimeCode,weaponCode,areaCode,premiseCode]
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });


    $('#submit-search').click(function () {
        // const tID = $('#task-form-display').attr('taskID');
        
        const eventVal = $('#search-modal').find('.form-control1').val()
        const col = document.getElementById("searchopts");
        console.log([eventVal,col.value])
        console.log("bruhhhh")
        $.ajax({
            type: 'POST',
            url:  '/search',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [eventVal,col.value]
            }),
            success: function (res) {
                console.log(res.response)
                window.location.assign("/search2")
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('delbutton').click(function () {
        var data = $.parseJSON($(this).attr('data-button'));
        console.log(data)

        // $.ajax({
        //     type: 'POST',
        //     url: '/delete/' + parseInt(data),
        //     success: function (res) {
        //         console.log(res.response)
        //         location.reload();
        //     },
        //     error: function () {
        //         console.log('Error');
        //     }
        // });
    });

    $('#userinserted').click(function () {
        $.ajax({
            type: 'POST',
            url: '/userinsert',
            success: function (res) {
                // window.location.href = '../../templates/advanced1.html'
                window.location.assign("/userinsert")
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#ages').click(function () {
        $.ajax({
            type: 'POST',
            url: '/agebreakdown',
            success: function (res) {
                // window.location.href = '../../templates/advanced1.html'
                window.location.assign("/agebreakdown")
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#weapons').click(function () {
        $.ajax({
            type: 'POST',
            url: '/weaponbreakdown',
            success: function (res) {
                // window.location.href = '../../templates/advanced1.html'
                window.location.assign("/weaponbreakdown")
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#advanced1').click(function () {
        $.ajax({
            type: 'POST',
            url: '/advanced1',
            success: function (res) {
                // window.location.href = '../../templates/advanced1.html'
                window.location.assign("/advanced1")
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#advanced2').click(function () {
        
        $.ajax({
            type: 'POST',
            url: '/advanced2',
            success: function (res) {
                // console.log(res.response)
                //print(res.response)
                window.location.assign("/advanced2")
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.state').click(function () {
        console.log("nahhh")
        const state = $(this)
        const tID = state.data('source')
        var new_state = ""
        if (state.text() === "In Progress") {
            new_state = "Complete"
        } else if (state.text() === "Complete") {
            new_state = "Todo"
        } else if (state.text() === "Todo") {
            new_state = "In Progress"
        }

        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});