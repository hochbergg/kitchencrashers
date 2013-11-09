
function initTypeahead(filter_element,$el,opts) {
    // Add the "Remove filter" footer
    opts.footer = "<div class='typeahead-seperator'></div><div class='tt-suggestion remove-filter-suggestion'><p>Remove Filter</p></div>";

    // Init the typeahead on our requested element
    $el.typeahead(opts);
    $el.data("ttView").setQuery($el.val()); // Force it to initialize, so it'll show options on click

    // If we empty the textboxt, remove the element
    $el.on("change",function() {
        if ($(this).val() === "") {
            filter_element.delete();
        }
    });

    // Events are registered on the parent element so we wont have to be dependant on typeahead.js's structure
    filter_element.$el.on("mouseleave",".remove-filter-suggestion",function() {
        $(this).removeClass("tt-is-under-cursor"); // We want to get the magical mouseover behaviour too
    });

    filter_element.$el.on("click",".remove-filter-suggestion",function() {
        filter_element.delete();
    });
}

function initDropdown(filter_element,$el,with_remove) {
    with_remove = typeof with_remove !== 'undefined' ? with_remove : true;

    if ( with_remove ) {
        remove_opts = '<li class="divider"></li><li><a href="#" class="remove-filter">Remove Filter</a></li>'

        $el.find(".dropdown-menu").append(remove_opts);

        $el.on("click",".remove-filter",function() {
            filter_element.delete();
        });
    }

    $el.on("click",".dropdown-option",function() {
        filter_element.val = {caption: $(this).text()};
        filter_element.render();
    });
}

$(function() {
    location_filter = new FilterElementType({
        name: "location",
        template: $("#location-filter-template")[0].innerHTML,
        initial_value: {caption: "Tel Aviv"},
        default_text: "at Tel Aviv",
        on_create: function(filter_element) {
            initTypeahead(filter_element,filter_element.$el.find(".location-search"),{
                local: ["Tel Aviv","Jerusalem","Petah Tikvah"]
            });
        }
    });

    category_filter = new FilterElementType({
        name: "category",
        template: $("#category-filter-template")[0].innerHTML,
        initial_value: {caption: "Italian Food"},
        default_text: "only Italian Food",
        on_create: function(filter_element) {
            initTypeahead(filter_element,filter_element.$el.find(".category-search"),{
                local: ["Italian Food","Asado","Chinese Food","Sushi"]
            });
        }
    });

    my_job_filter = new FilterElementType({
        name: "my_job",
        template: $("#my-job-filter-template")[0].innerHTML,
        initial_value: {caption: "Cook"},
        default_text: "Cook",
        on_create: function(filter_element) {
            initDropdown(filter_element,filter_element.$el,false);
        }
    });

    meal_filter = new FilterElementType({
        name: "meal",
        template: $("#meal-filter-template")[0].innerHTML,
        initial_value: {caption: "Dinner"},
        default_text: "for Dinner",
        on_create: function(filter_element) {
            initDropdown(filter_element,filter_element.$el);
        }
    });

    price_filter = new FilterElementType({
        name: "price",
        template: $("#price-filter-template")[0].innerHTML,
        initial_value: {min: 50, max: 100},
        default_text: "for 50 to 100 NIS",
        on_create: function(filter_element) {
            initTypeahead(filter_element,filter_element.$el.find(".money-from"),{local: []});
            initTypeahead(filter_element,filter_element.$el.find(".money-to"),{local: []});
        }
    });

    fg = new FilterGroup($("#search-form"), $("#add-filter-template")[0].innerHTML);
    fg.add_type(location_filter);
    fg.add_type(category_filter);
    fg.add_type(my_job_filter);
    fg.add_type(price_filter);
    fg.add_type(meal_filter);

    fg.create("my_job");
    fg.create("location");
    fg.create("category");
});