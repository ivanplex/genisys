# Configurator

Short name for gas-spring configurator is a special purpose configurator for creating gas spring orders.

## Component factor

Component factor (CF) is used to determine the internal offset of a combined length, where the total length of component A attached to component B is less than the sum of both components.

Component factor are given to each **atomic component** and **blueprints**. 

In the case of **atomic component**, they are given a CF of `0.0` by default unless specified explicitly.

For **blueprints** however, CF can either be specified on unspecified. 

**Specified:**
> When CF is specified for a blueprint, it would ignore all CF in its dependency and directly return its specified component factor when `getComponentFactor()` is called.
>
> E.g. **Blueprint B** has a CF of `5` with dependency **Component X**(CF: `8`) and **Component Y**(CF: `10`). By calling `getComponentFactor()` on **Blueprint B** will give you `5`, ignoring CF in component X and Y.

**Unspecified:**
> If CF is not specified, it means that there is no component factor implyed at this level. However it does not mean CF does not exist at lower levels (its dependencies). In such case, the function `getComponentFactor()` will then look for CF factor of its dependency and take the sum of it. 
>
> E.g. **Blueprint B** has a CF of `None` with dependency **Component X**(CF: `8`) and **Component Y**(CF: `10`). By calling `getComponentFactor()` on **Blueprint B** will give you `18`.


