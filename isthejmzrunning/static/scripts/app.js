$(document).ready(function() {
  const notRunningText = 'Not running... bummer!';
  const delayText = 'Delayed :(';
  const goodText = 'All good!';
  const listContainer = $('<ul>', {class: 'list_container'});

  $.get('fetch', function(lineStatuses) {
    $('.data_container').html(listContainer);

    lineStatuses = JSON.parse(lineStatuses);

    for (let i = 0; i < lineStatuses.length; i++) {
      let statusText;

      if (lineStatuses[i].not_running) {
        statusText = notRunningText;
      } else if (lineStatuses[i].delay_status) {
        statusText = delayTextl
      } else {
        statusText = goodText;
      }

      $('<li>').html(lineStatuses[i].route_id + ': ' + statusText).appendTo(listContainer)
    }
  });
})