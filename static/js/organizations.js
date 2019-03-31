$(document).ready(() => {

    $('#submit-btn').click(() => {
        const orgName = $('#org-name').val().trim();
        const foodChecked = $('#food-check').prop('checked');
        const hygieneChecked = $('#hygiene-check').prop('checked');
        const shelterChecked = $('#shelter-check').prop('checked');
        const address = $('#address').val().trim();
        const phoneNumber = $('#phone-number').val().trim();
        const website = $('#website').val().trim();

        const typesArray = []
        if(foodChecked == true) {
            typesArray.push('food');
        }

        if(hygieneChecked == true) {
            typesArray.push('hygiene');
        }

        if(shelterChecked == true) {
            typesArray.push('shelter');
        }

        const newOrg = {
            [orgName]: {
                "types": typesArray,
                "website": website,
                "phone": phoneNumber,
                "name": orgName,
                "location": address
            }
        };

        console.log(newOrg);

        // i literally don't know what to do
        
        $.post('/add-new-org', {
                 "types": typesArray,
                 "website": website,
                 "phone": phoneNumber,
                 "name": orgName,
                 "location": address
        });
    });

});