'use strict';

// Class definition
var KTDualListbox = function() {

  // Private functions
  var initDualListbox = function() {
    // Dual Listbox
    var listBoxes = $('.kt-dual-listbox');
    var listBoxCausas = $('#kt-dual-listbox-causas');

    listBoxes.each(function() {
      var $this = $(this);
      // get titles
      var availableTitle = ($this.attr('data-available-title') != null) ? $this.attr('data-available-title') : 'Opciones disponibles';
      var selectedTitle = ($this.attr('data-selected-title') != null) ? $this.attr('data-selected-title') : 'Opciones seleccionadas';

      // get button labels
      var addLabel = ($this.attr('data-add') != null) ? $this.attr('data-add') : 'Agregar';
      var removeLabel = ($this.attr('data-remove') != null) ? $this.attr('data-remove') : 'Eliminar';
      var addAllLabel = ($this.attr('data-add-all') != null) ? $this.attr('data-add-all') : 'Agregar Todos';
      var removeAllLabel = ($this.attr('data-remove-all') != null) ? $this.attr('data-remove-all') : 'Eliminar Todos';

      // get options
      var options = [];
      $this.children('option').each(function() {
        var value = $(this).val();
        var label = $(this).text();
        var selected = !!($(this).is(':selected'));
        options.push({text: label, value: value, selected: selected});
      });

      // get search option
      var search = ($this.attr('data-search') != null) ? $this.attr('data-search') : '';

      // clear duplicates
      $this.empty();

      // init dual listbox
      var dualListBox = new DualListbox($this.get(0), {
        addEvent: function(value) {          
          var identificador_riesgo_creado = $("#identificador-riesgo-creado").html();
          $.ajax({
            url:'/crea-riesgo/registra-causa-consecuencia',
            type:'GET',
            dataType:'json',
            data:{'valor':value, 'identificador_riesgo_creado':identificador_riesgo_creado},
            success:function(data){
              console.log(data);
            }, error(err){
              console.error(err);
              alert("Ha ocurrido un error al registrar.-");
            }
          })
        },
        removeEvent: function(value) {
          var identificador_riesgo_creado = $("#identificador-riesgo-creado").html();
          $.ajax({
            url:'/crea-riesgo/elimina-causa-consecuencia',
            type:'GET',
            dataType:'json',
            data:{'valor':value, 'identificador_riesgo_creado':identificador_riesgo_creado},
            success:function(data){
              console.log(data);
            }, error(err){
              alert("Ha ocurrido un error al eliminar.-");
              console.error(err);
            }
          })
        },
        availableTitle: availableTitle,
        selectedTitle: selectedTitle,
        addButtonText: addLabel,
        removeButtonText: removeLabel,
        addAllButtonText: addAllLabel,
        removeAllButtonText: removeAllLabel,
        options: options,
      });

      if (search == 'false') {
        dualListBox.search.classList.add('dual-listbox__search--hidden');
      }
    });  

  };

  return {
    // public functions
    init: function() {
      initDualListbox();
    },
  };
}();

KTUtil.ready(function() {
  KTDualListbox.init();
});
