function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

$(document).ready(() => {
  const notRunningText = ['Not running. Bummer!', 'Not in service.'];
  const delayText = ['Delayed :(', 'Looks delayed. You look great!', 'Delayed. Damn!'];
  const goodText = ['All good!', 'Cool runnings!', 'Looks good. You, too!'];
  const routeContainer = $('<div>');
  const errorContainer = $('<div>', { class: 'error_container' }).html('Sorry, there was an error. Please refresh.');
  const brownRouteClass = 'brown_route';
  const orangeRouteClass = 'orange_route';

  $.get('/api/fetch', (routeStatuses) => {
    const parsedRouteStatuses = JSON.parse(routeStatuses);

    if (parsedRouteStatuses) {
      $('.data_container').html(routeContainer);

      for (let i = 0; i < parsedRouteStatuses.length; i += 1) {
        const routeInfoContainer = $('<div>', { class: `route_info col-xs-12 ${parsedRouteStatuses[i].route_id === 'M' ? orangeRouteClass : brownRouteClass}` });
        const routeIdSpan = $('<span>', { class: 'route_id_span' }).text(parsedRouteStatuses[i].route_id);
        let statusText;

        if (parsedRouteStatuses[i].not_running) {
          statusText = notRunningText[getRandomInt(notRunningText.length)];
        } else if (parsedRouteStatuses[i].delay_status) {
          statusText = delayText[getRandomInt(delayText.length)];
        } else {
          statusText = goodText[getRandomInt(goodText.length)];
        }

        const statusTextSpan = $('<span>', { class: 'status_text_span' }).text(statusText);

        routeInfoContainer
          .html(`${routeIdSpan[0].outerHTML} ${statusTextSpan[0].outerHTML}`)
          .appendTo(routeContainer);
      }
    } else {
      $('.data_container').html(errorContainer);
    }
  });
});
