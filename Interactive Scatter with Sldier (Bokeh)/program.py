from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Slider, CustomJS
from bokeh.layouts import column

x = list(range(10))
y = [i**2 for i in x]
source = ColumnDataSource(data=dict(x=x, y=y))

p = figure(title="Interactive Scatter with Slider",
           x_axis_label="x", y_axis_label="y")
p.circle("x", "y", size=10, source=source, color="green")

slider = Slider(start=1, end=5, value=1, step=1, title="Multiplier")
slider.js_on_change("value", CustomJS(args=dict(source=source, slider=slider),
    code="""
        var data = source.data;
        var f = slider.value;
        data['y'] = data['x'].map(x => x*x*f);
        source.change.emit();
    """))

show(column(slider, p))
