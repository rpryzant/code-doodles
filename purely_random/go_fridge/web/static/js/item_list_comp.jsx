var ItemList = React.createClass({

  getInitialState: function() {
    return {
      error: false,
      items: [],
    };
  },

  componentDidMount: function() {
    this.getData();   
  },

  getData: function() {
    $.getJSON('/items')
      .done(function(data) {
        this.setState({items: data.items});
      }.bind(this)).fail(function() {
        this.setState({error: true});
      }.bind(this));
  },

  render: function() {
    var error;
    if (this.state.error) {
      error = <p>An error occured when making the request</p>;
    }

    var getItemView = function(item) {
      return <ItemView key={item} item={item} />;
    };

    var items = this.state.items;
    return (
      <div className="items row">
        {error}
        <div className="col-md-2 more-style">
          {items.slice(0, items.length/2 + 1).map(getItemView)}
        </div>
        <div className="col-md-8">
          <img src={window.fridgeImageSrc} className="img-responsive narrow-image" id="fridge-img" />
        </div>
        <div className="col-md-2 more-style">
          {items.slice(items.length/2 + 1, items.length).map(getItemView)}
        </div>
      </div>
    );
  },

});
