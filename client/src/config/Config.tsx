import * as React from 'react';

// Hello Alex
// Essentially we want a component that's mounted on this page to edit something of this schema:

// [
//   {
//     prompt_key: 'site', // str, uniq_id
//     prompt_text: 'Where are you picking?',  // str
//     response_type: 'choice' | 'text' // is the response multi-choice or free text
//     response_options: ['face', 'lip', 'hair'] // exists if response_type == 'choice'
//   },
//   {
//     prompt_key: 'another_example',
//     prompt_text: 'Where are you?',
//     prompt_type: 'text'
//   },
// ]

// props
// 1. json of old config
// 2. handler to callback with new config json
export default class Config extends React.Component {
  public render(): JSX.Element {
    return(
      <div>
        This is page for configuring treatment flows.
      </div>
    );
  }
}
