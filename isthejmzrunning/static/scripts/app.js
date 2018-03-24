$(document).ready(function() {
  const notRunningText = 'Not running... bummer!';
  const delayText = 'Delayed :(';
  const goodText = 'All good!';
  const routeContainer = $('<div>');
  const brownRouteClass = 'brown_route';
  const orangeRouteClass = 'orange_route';

  $.get('fetch', function(routeStatuses) {
    $('.data_container').html(routeContainer);

    routeStatuses = JSON.parse(routeStatuses);

    for (let i = 0; i < routeStatuses.length; i++) {
      let statusText;

      if (routeStatuses[i].not_running) {
        statusText = notRunningText;
      } else if (routeStatuses[i].delay_status) {
        statusText = delayTextl
      } else {
        statusText = goodText;
      }

      $('<div>', {class: 'routeInfo col-xs-12 ' + (routeStatuses[i].route_id === 'M' ? orangeRouteClass : brownRouteClass)})
        .html('<span class=\'route_id_span\'>' + routeStatuses[i].route_id + '</span>' + ' ' + statusText)
        .appendTo(routeContainer);
    }
  });
})