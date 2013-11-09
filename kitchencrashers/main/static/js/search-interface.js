FilterElementType = function(def) {
    this.name = def.name;
    this.template = Hogan.compile(def.template,{delimiters: "[[ ]]"});
    this.initial_value = def.initial_value;
    this.default_text = def.default_text;
    this.on_create = def.on_create;
    this.getValue = def.getValue;
}

FilterElementType.prototype.create = function(filter_group,$el) {
    return new FilterElement(filter_group,this,this.initial_value,$el);
}

FilterElement = function(filter_group,type,value,$el) {
    this.$el = $el;
    this.type = type;
    this.val = value;
    this.filter_group = filter_group;
    this.render();
    this.type.on_create(this);
}

FilterElement.prototype.render = function() {
    this.$el.html(this.type.template.render(this.val));
}

FilterElement.prototype.delete = function() {
    this.$el.remove();
    this.filter_group.remove_element(this);
}

FilterElement.prototype.getValue = function() {
    return this.type.getValue(this,this.$el);
}

FilterGroup = function($el,add_filter_template,onChange) {
    this.$el = $el;
    this.filters = []
    this.filter_types = {}
    this.add_filter_template = Hogan.compile(add_filter_template,{delimiters: "[[ ]]"});

    if (typeof(onChange) == 'undefined') {
        onChange = function() {}
    }

    this._onChange = onChange;

    var me = this; // For the closure
    this.$el.on("click",".add-filter-link",function(e) {
        me.create($(this).data("filter"));
        e.stopPropagation();
        return false;
    });

    this.update_left_dropdown();
}

FilterGroup.prototype.onChange = function(element) {
    this._onChange(this);
}

FilterGroup.prototype.remove_element = function(element) {
    index = this.filters.indexOf(element);

    if (index != -1) {
        this.filters.splice(index,1)
    }

    this.update_left_dropdown();
    this.onChange();
}

FilterGroup.prototype.add_type = function(type) {
    this.filter_types[type.name] = type;

    this.update_left_dropdown();
}

FilterGroup.prototype.create = function(type_name) {
    type = this.filter_types[type_name];
    $new_el = $("<div></div>");
    $new_el.addClass("filter-element");
    this.$el.find(".filters").append($new_el);

    this.filters.push(type.create(this,$new_el));
    this.update_left_dropdown();
    this.onChange();
}

FilterGroup.prototype.update_left_dropdown = function() {
    left = this.find_left_filters();

    out = []

    for (var name in left) {
        out.push({name: name,
            text: left[name].default_text});
    }

    if (out.length > 0) {
        this.$el.find(".add-filter").show();
        this.$el.find(".add-filter").html(this.add_filter_template.render({filters: out}));
    } else {
        this.$el.find(".add-filter").hide();
    }
        
}

FilterGroup.prototype.find_left_filters = function() {
    left = {}
    for(var name in this.filter_types) {
        left[name] = this.filter_types[name];
    }

    for(var i=0;i<this.filters.length;i++) {
        delete left[this.filters[i].type.name];
    }

    return left
}

FilterGroup.prototype.toQuery = function() {
    out = {}
    for(var i=0;i<this.filters.length;i++) {
        name = this.filters[i].type.name;
        if (!(name in out)) {
            out[name] = []
        }

        out[name].push(this.filters[i].getValue());
    }

    return out;
}