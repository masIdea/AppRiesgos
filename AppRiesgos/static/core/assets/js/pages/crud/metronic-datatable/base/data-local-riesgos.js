'use strict';
// Class definition

var KTDatatableDataLocalDemo = function() {
	// Private functions

	// demo initializer
	var demo = function() {
        var dataJSONArray = JSON.parse('[{"num":"1", "gerencia":"GPRO","monto_mmusd":"13.275","porc_monto":"88","cantidad":"3","porc_cantidad":"8,6","Actions":null, "kpi":null},\n' +                                        
                                        '{"num":"2","gerencia":"GMIN","monto_mmusd":"903","porc_monto":"6","cantidad":"20","porc_cantidad":"20","Actions":null, "kpi":null},\n' +
										'{"num":"3","gerencia":"GSYS","monto_mmusd":"308","porc_monto":"2","cantidad":"6","porc_cantidad":"7,5","Actions":null, "kpi":null},\n' +
										'{"num":"4","gerencia":"GOBM","monto_mmusd":"607","porc_monto":"4","cantidad":"44","porc_cantidad":"55","Actions":null, "kpi":null},\n' +										
										'{"num":"5","gerencia":"GDI","monto_mmusd":"100","porc_monto":"7","cantidad":"10","porc_cantidad":"12","Actions":null, "kpi":null},\n' +
										'{"num":"6","gerencia":"GPTA","monto_mmusd":"100","porc_monto":"23","cantidad":"10","porc_cantidad":"5,5","Actions":null, "kpi":null},\n' +
										'{"num":"7","gerencia":"GRHU","monto_mmusd":"100","porc_monto":"22","cantidad":"10","porc_cantidad":"9,3","Actions":null, "kpi":null},\n' +
										'{"num":"8","gerencia":"GRMD","monto_mmusd":"100","porc_monto":"56","cantidad":"10","porc_cantidad":"57,4","Actions":null, "kpi":null},\n' +
										'{"num":"9","gerencia":"GRSW","monto_mmusd":"100","porc_monto":"29","cantidad":"10","porc_cantidad":"56","Actions":null, "kpi":null},\n' +
										'{"num":"10","gerencia":"GSAE","monto_mmusd":"100","porc_monto":"17","cantidad":"10","porc_cantidad":"8,1","Actions":null, "kpi":null},\n' +
										'{"num":"11","gerencia":"GSSO","monto_mmusd":"100","porc_monto":"19","cantidad":"10","porc_cantidad":"45,2","Actions":null, "kpi":null},\n' +
										'{"num":"12","gerencia":"GFUN","monto_mmusd":"100","porc_monto":"29","cantidad":"10","porc_cantidad":"78,9","Actions":null, "kpi":null},\n' +
										'{"num":"13","gerencia":"GTRH","monto_mmusd":"100","porc_monto":"34","cantidad":"10","porc_cantidad":"80","Actions":null, "kpi":null}]' 
                                        /*'{"gerencia":"GDI","monto_mmusd":"China","porc_monto":"CN","cantidad":"Jiujie","porc_cantidad":"Rempel Inc","Actions":null},\n' +
                                        '{"gerencia":"GPTA","monto_mmusd":"China","porc_monto":"CN","cantidad":"Jiujie","porc_cantidad":"Rempel Inc","Actions":null},\n' +
                                        '{"gerencia":"GRHU","monto_mmusd":"China","porc_monto":"CN","cantidad":"Jiujie","porc_cantidad":"Rempel Inc","Actions":null},\n' +
                                        '{"gerencia":"GRMD","monto_mmusd":"China","porc_monto":"CN","cantidad":"Jiujie","porc_cantidad":"Rempel Inc","Actions":null},\n' +
                                        '{"gerencia":"GRSW","monto_mmusd":"China","porc_monto":"CN","cantidad":"Jiujie","porc_cantidad":"Rempel Inc","Actions":null},\n' +
                                        '{"gerencia":"GSAE","monto_mmusd":"China","porc_monto":"CN","cantidad":"Jiujie","porc_cantidad":"Rempel Inc","Actions":null},\n' +
                                        '{"gerencia":"GSSO","monto_mmusd":"China","porc_monto":"CN","cantidad":"Jiujie","porc_cantidad":"Rempel Inc","Actions":null},\n' +
                                        '{"gerencia":"GSYS","monto_mmusd":"China","porc_monto":"CN","cantidad":"Jiujie","porc_cantidad":"Rempel Inc","Actions":null},\n' +
                                        '{"gerencia":"GTRH","monto_mmusd":"China","porc_monto":"CN","cantidad":"Jiujie","porc_cantidad":"Rempel Inc","Actions":null}]'   */
        );

		var datatable = $('.kt-datatable').KTDatatable({
			// datasource definition
			data: {
				type: 'local',
				source: dataJSONArray,
				pageSize: 5,
			},

			// layout definition
			layout: {
				scroll: false, // enable/disable datatable scroll both horizontal and vertical when needed.
				// height: 450, // datatable's body's fixed height
				footer: false, // display/hide footer
			},

			// column sorting
			sortable: true,

			pagination: true,

			search: {
				input: $('#generalSearch'),
			},

			// columns definition
			columns: [	
				{
					field: 'num',
					title: '#',
				},	
                {
					field: 'gerencia',
					title: 'Gerencia',
				},{
					field: 'monto_mmusd',
					title: 'Monto MMUSD',
				}, {
					field: 'porc_monto',
					title: '% MONTO',
					//template: function(row) {
					//	return row.Country + ' ' + row.ShipCountry;
					//},
				}, {
					field: 'cantidad',
					title: 'Cantidad',
					//type: 'date',
					//format: 'MM/DD/YYYY',
				}, {
					field: 'porc_cantidad',
					title: '% Cantidad',
				}, {
					field: 'Actions',
					title: 'Acciones',
					sortable: false,
					width: 110,
					overflow: 'visible',
					autoHide: false,
					template: function(row) {
												
						return '\
						\
						<a href="javascript:;" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="Aplicar Filtro">\
							<i class="la la-filter"></i>\
						</a>\
						<a href="javascript:;" onclick="modal_matriz(\''+row.gerencia+'\')" class="btn btn-sm btn-clean btn-icon btn-icon-md" title="Ver">\
							<i class="la la-eye"></i>\
						</a>\
					';
					},
				},{
					field: 'kpi',
					title: 'Indicador',
					sortable: false,
					width: 110,
					overflow: 'visible',
					autoHide: false,
					template: function(row) {
						if(row.gerencia == "GPRO" || row.gerencia == "GMIN" || row.gerencia == "GSYS" || row.gerencia == "GOBM"){
							return '\
							<span class="dot" style="height: 15px;width: 15px;background-color: #f34747;border-radius: 50%;display: inline-block;"></span>\
					';
						}else{
							return '\
							&nbsp;\
					';
						}
						

					},
				}],
		});

		$('#kt_form_status').on('change', function() {
			datatable.search($(this).val().toLowerCase(), 'Status');
		});

		$('#kt_form_type').on('change', function() {
			datatable.search($(this).val().toLowerCase(), 'Type');
		});

		$('#kt_form_status,#kt_form_type').selectpicker();

	};

	return {
		// Public functions
		init: function() {
			// init dmeo
			demo();
		},
	};
}();

jQuery(document).ready(function() {
	setTimeout(() => {
		KTDatatableDataLocalDemo.init();
	}, 5000);	
});

var modal_matriz = function(gerencia){
	$("#span_gerencia").html(gerencia);
	$("#modal_matrices").modal("show");
}