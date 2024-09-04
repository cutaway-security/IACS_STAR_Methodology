/*!
 * calc v0.0.1
 * Calculator functions for generating results
 * MIT License
 */
window.onload = function() {
    // Call the function when the page loads
    const decodedVector = getDecodedVectorFromUrl();
    if (decodedVector){
        init(decodedVector,'')
        colorize()
    }
    console.log(decodedVector);
};

function getDecodedVectorFromUrl() {
    // Get the full URL
    const url = window.location.href;

    // Create a URL object
    const urlObj = new URL(url);

    // Get the 'vector' parameter from the URL
    const vectorParam = urlObj.searchParams.get('vector');

    if (vectorParam) {
        // Base64 decode the 'vector' parameter
        try {
            // Decode the base64 string
            const decodedVector = atob(vectorParam);
            return decodedVector;
        } catch (error) {
            console.error('Error decoding vector parameter:', error);
            return null;
        }
    } else {
        console.error('No vector parameter found in the URL.');
        return null;
    }
}

function update_form() {
    init($('#vector-input').val(), '')
    colorize()
}

function init(vector, v) {
    var i = 0;
    var part = '';
    var partials = ["sl", "m", "o", "a", "ea", "ee", "aw", "dr", "lc", "li", "la", "lac", "ed", "pd", "se", "r"];
    for (var i = 0; i < partials.length; i++) {
        $("#" + partials[i]).val(0);
    }
    var reg = /^\d+$/;
    if (reg.test(v) && v.length == 16) {
        for (var i = 0; i < v.length; i++) {
            $("#" + partials[i].toLowerCase()).val(parseInt(v[i]));
        }
    } else {
        vector = vector.replace('(', '').replace(')', '');
        var values = vector.split('/');
        for (var i = 0; i <= values.length - 1; i++) {
            part = values[i].split(':');
            if (part.length == 2) {
                if (partials.indexOf(part[0].toLowerCase()) >= 0 && ! isNaN(parseInt(part[1])) && parseInt(part[1]) >= 0 && parseInt(part[1]) <= 9) {
                    $("#" + part[0].toLowerCase()).val(parseInt(part[1]));
                }
            }
        }
    }
}

function colorize() {
    $('.custom-select').each(function() {
        $(this).removeClass('text-0 text-1 text-2 text-3 text-4 text-5 text-6 text-7 text-8 text-9');
        $(this).addClass('text-' + $(this).val());
    });
}
function getRisk(score) {
    if(score == 0) return 'Informational';
    if(score <  3) return 'Low';
    if(score <  6) return 'Medium';
    if(score <= 9) return 'High';
}

function getRiskInNum(score) {
    if(score <  3) return 0;
    if(score <  6) return 1;
    if(score <= 9) return 2;
}

function setFactor(factor, sFactor) {
    $('#' + sFactor).parent().removeClass('text-Note text-Low text-Medium text-High text-Critical').addClass('text-' + getRisk(factor));
    $('#' + sFactor).text(getRisk(factor)+' ('+sFactor+': '+factor+')');

}

function calculate() {
    var TAF, VF, TIF, SIF, LF, CF, R, mLF, mCF = 0;
    var score = '';
    var matrix = [];
    matrix[0] = [];
    matrix[1] = [];
    matrix[2] = [];
    TAF = (+ $("#sl").val() + +$("#m").val() + +$("#o").val() + +$("#a").val()) / 4;
    VF = (+$("#ea").val() + +$("#ee").val() + +$("#aw").val() + +$("#dr").val()) / 4;
    TIF = (+ ($("#lc").val()  * 1 )+ +($("#li").val() * 1 )
            + + ($("#la").val()* 1 ) + + ($("#lac").val() * 1 )) / 4;
    SIF = (+($("#ed").val() * 1 ) + +($("#pd").val()  * 1 )
            + +($("#se").val()  * 1 )+ +($("#r").val() * 1 )) / 4;
    score = '(';
    score = score + 'SL:' + $("#sl").val() + '/';
    score = score + 'M:' + $("#m").val() + '/';
    score = score + 'O:' + $("#o").val() + '/';
    score = score + 'A:' + $("#a").val() + '/';
    score = score + 'EA:' + $("#ea").val() + '/';
    score = score + 'EE:' + $("#ee").val() + '/';
    score = score + 'AW:' + $("#aw").val() + '/';
    score = score + 'DR:' + $("#dr").val() + '/';
    score = score + 'LC:' + $("#lc").val() + '/';
    score = score + 'LI:' + $("#li").val() + '/';
    score = score + 'LA:' + $("#la").val() + '/';
    score = score + 'LAC:' + $("#lac").val() + '/';
    score = score + 'ED:' + $("#ed").val() + '/';
    score = score + 'PD:' + $("#pd").val() + '/';
    score = score + 'SE:' + $("#se").val() + '/';
    score = score + 'R:' + $("#r").val();
    score = score + ')';
    score_param = btoa(score)
    
    $('#score').text(score);
    $("#score").attr("href", "https://iacs-star-calculator.com/html/iacs_star_calculator.html?vector=" + score_param);
    matrix[0][0] = 'Informational';
    matrix[1][0] = 'Low';
    matrix[2][0] = 'Medium';
    matrix[0][1] = 'Low';
    matrix[1][1] = 'Medium';
    matrix[2][1] = 'High';
    matrix[0][2] = 'Medium';
    matrix[1][2] = 'High';
    matrix[2][2] = 'Critical';
    LF = (TAF + VF) / 2;
    CF = (TIF + SIF) / 2;
    /*
    if (SIF != 0) {
        CF = SIF;
    } else {
        CF = TIF;
    }
    */
    setFactor(TAF, 'TAF');
    setFactor(VF, 'VF');
    setFactor(TIF, 'TIF');
    setFactor(SIF, 'SIF');
    setFactor(LF, 'LF');
    setFactor(CF, 'CF');
    if (LF != 0 && CF != 0) {
    }
    mLF = getRiskInNum(LF);
    mCF = getRiskInNum(CF);
    $('#Risk').parent().removeClass('text-Note text-Low text-Medium text-High text-Critical').addClass('text-' + matrix[mLF][mCF]);
    $('#Risk').text(matrix[mLF][mCF]);
}

function getUrlParameter(name) {
    name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
    var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    var results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
};  

$(document).ready(function() {
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
    $('.custom-select').change(function() {
        $(this).removeClass('text-0 text-1 text-2 text-3 text-4 text-5 text-6 text-7 text-8 text-9');
        $(this).addClass('text-' + $(this).val());
        calculate();
    });
    init(atob(getUrlParameter('vector')), getUrlParameter('v'));
    colorize();
    calculate();
});                  
});