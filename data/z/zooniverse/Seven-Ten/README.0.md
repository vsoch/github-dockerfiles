## Structure

Authorization is provided by a [JWT](https://tools.ietf.org/html/rfc7523) token from [Panoptes](https://github.com/zooniverse/Panoptes) sent in the request's `Authorization` header.

[Policies](https://github.com/zooniverse/Seven-Ten/blob/master/app/policies)
  - what actions are allowed for a user

[Schemas](https://github.com/zooniverse/Seven-Ten/blob/master/app/schemas)
  - what parameters are required for an action

[Serializers](https://github.com/zooniverse/Seven-Ten/blob/master/app/serializers)
  - how resources are presented
  - what associations can be included
  - what parameters can be used for filtering or sorting

## Resources

[Examples](https://github.com/zooniverse/Seven-Ten/blob/master/docs/examples.md)
  - A few examples of creating splits and variants on the Rails console.

[Project](https://github.com/zooniverse/Seven-Ten/blob/master/docs/projects.md)
  - A local representation of a [Panoptes](https://github.com/zooniverse/Panoptes) project

[Split](https://github.com/zooniverse/Seven-Ten/blob/master/docs/splits.md)
  - The A/B split test

[Variant](https://github.com/zooniverse/Seven-Ten/blob/master/docs/variants.md)
  - A split variant

[SplitUserVariant](https://github.com/zooniverse/Seven-Ten/blob/master/docs/split_user_variants.md)
  - The assignment of Variant to a User for a Split

[Metric](https://github.com/zooniverse/Seven-Ten/blob/master/docs/metrics.md)
  - The record of a user event

[DataRequest](https://github.com/zooniverse/Seven-Ten/blob/master/docs/data_requests.md)
  - A request for a Split's Metrics
