function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

$(document).ready(function() {
  const notRunningText = ['Not running... bummer!', 'Not in service.', 'Seems like it\'s not running...'];
  const delayText = ['Delayed :(', 'Looks like delays... but you look great!', 'Delayed - damn!'];
  const goodText = ['All good!', 'Cool runnings!', 'Looks good... and so do you!'];
  const routeContainer = $('<div>');
  const brownRouteClass = 'brown_route';
  const orangeRouteClass = 'orange_route';

  $.get('/api/fetch', function(routeStatuses) {
    $('.data_container').html(routeContainer);

    routeStatuses = JSON.parse(routeStatuses);

    for (let i = 0; i < routeStatuses.length; i++) {
      const routeInfoContainer = $('<div>', {class: 'route_info col-xs-12 ' + (routeStatuses[i].route_id === 'M' ? orangeRouteClass : brownRouteClass)});
      const routeIdSpan = $('<span>', {class: 'route_id_span'}).text(routeStatuses[i].route_id);
      let statusText;

      if (routeStatuses[i].not_running) {
        statusText = notRunningText[getRandomInt(notRunningText.length)];
      } else if (routeStatuses[i].delay_status) {
        statusText = delayText[getRandomInt(delayText.length)];
      } else {
        statusText = goodText[getRandomInt(goodText.length)];
      }

      const statusTextSpan = $('<span>', {class: 'status_text_span'}).text(statusText);

      routeInfoContainer
        .html(routeIdSpan[0].outerHTML + ' ' + statusTextSpan[0].outerHTML)
        .appendTo(routeContainer);
    }
  });
})