memory_1="""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex, nofollow" />
<meta content="width=device-width, initial-scale=1" name="viewport">
<meta name="description" content="Morrison Game Company Server">
<link rel="icon" type="image/png" href="favicon.png">
<title>Morrison Game Factory</title>
<style title="Twine CSS">@keyframes appear{0%{opacity:0}to{opacity:1}}@keyframes fade-in-out{0%,to{opacity:0}50%{opacity:1}}@keyframes rumble{25%{top:-0.1em}75%{top:.1em}0%,to{top:0px}}@keyframes shudder{25%{left:.1em}75%{left:-0.1em}0%,to{left:0px}}@keyframes buoy{25%{top:.25em}75%{top:-0.25em}0%,to{top:0px}}@keyframes sway{25%{left:.25em}75%{left:-0.25em}0%,to{left:0px}}@keyframes pulse{0%{transform:scale(0, 0)}20%{transform:scale(1.2, 1.2)}40%{transform:scale(0.9, 0.9)}60%{transform:scale(1.05, 1.05)}80%{transform:scale(0.925, 0.925)}to{transform:scale(1, 1)}}@keyframes zoom-in{0%{transform:scale(0, 0)}to{transform:scale(1, 1)}}@keyframes shudder-in{0%,to{transform:translateX(0em)}5%,25%,45%{transform:translateX(-1em)}15%,35%,55%{transform:translateX(1em)}65%{transform:translateX(-0.6em)}75%{transform:translateX(0.6em)}85%{transform:translateX(-0.2em)}95%{transform:translateX(0.2em)}}@keyframes rumble-in{0%,to{transform:translateY(0em)}5%,25%,45%{transform:translateY(-1em)}15%,35%,55%{transform:translateY(1em)}65%{transform:translateY(-0.6em)}75%{transform:translateY(0.6em)}85%{transform:translateY(-0.2em)}95%{transform:translateY(0.2em)}}@keyframes fidget{0%,8.1%,82.1%,31.1%,38.1%,44.1%,40.1%,47.1%,74.1%,16.1%,27.1%,72.1%,24.1%,95.1%,6.1%,36.1%,20.1%,4.1%,91.1%,14.1%,87.1%,to{left:0px;top:0px}8%,82%,31%,38%,44%{left:-1px}40%,47%,74%,16%,27%{left:1px}72%,24%,95%,6%,36%{top:-1px}20%,4%,91%,14%,87%{top:1px}}@keyframes slide-right{0%{transform:translateX(-100vw)}}@keyframes slide-left{0%{transform:translateX(100vw)}}@keyframes slide-up{0%{transform:translateY(100vh)}}@keyframes slide-down{0%{transform:translateY(-100vh)}}@keyframes fade-right{0%{opacity:0;transform:translateX(-1em)}to{opacity:1}}@keyframes fade-left{0%{opacity:0;transform:translateX(1em)}to{opacity:1}}@keyframes fade-up{0%{opacity:0;transform:translateY(1em)}to{opacity:1}}@keyframes fade-down{0%{opacity:0;transform:translateY(-1em)}to{opacity:1}}@keyframes flicker{0%,29%,31%,63%,65%,77%,79%,86%,88%,91%,93%{opacity:0}30%{opacity:.2}64%{opacity:.4}78%{opacity:.6}87%{opacity:.8}92%,to{opacity:1}}@keyframes blur{0%{filter:blur(2rem);opacity:0}25%{opacity:1}to{filter:blur(0rem);opacity:1}}.dom-debug-mode tw-story,.dom-debug-mode tw-passage,.dom-debug-mode tw-sidebar,.dom-debug-mode tw-include,.dom-debug-mode tw-hook,.dom-debug-mode tw-expression,.dom-debug-mode tw-link,.dom-debug-mode tw-dialog,.dom-debug-mode tw-columns,.dom-debug-mode tw-column,.dom-debug-mode tw-align{outline:1px solid #f5a3da;min-height:32px;display:block !important}.dom-debug-mode tw-story::before,.dom-debug-mode tw-passage::before,.dom-debug-mode tw-sidebar::before,.dom-debug-mode tw-include::before,.dom-debug-mode tw-hook::before,.dom-debug-mode tw-expression::before,.dom-debug-mode tw-link::before,.dom-debug-mode tw-dialog::before,.dom-debug-mode tw-columns::before,.dom-debug-mode tw-column::before,.dom-debug-mode tw-align::before{position:absolute;top:0;left:0;height:16px;background-color:#f5a3da;color:#000;font-size:16px;font-weight:normal;font-style:normal;font-family:monospace;display:inline-block;line-height:100%;white-space:pre;z-index:999997}.dom-debug-mode tw-story:hover,.dom-debug-mode tw-passage:hover,.dom-debug-mode tw-sidebar:hover,.dom-debug-mode tw-include:hover,.dom-debug-mode tw-hook:hover,.dom-debug-mode tw-expression:hover,.dom-debug-mode tw-link:hover,.dom-debug-mode tw-dialog:hover,.dom-debug-mode tw-columns:hover,.dom-debug-mode tw-column:hover,.dom-debug-mode tw-align:hover{outline:1px solid #fc9}.dom-debug-mode tw-story:hover::before,.dom-debug-mode tw-passage:hover::before,.dom-debug-mode tw-sidebar:hover::before,.dom-debug-mode tw-include:hover::before,.dom-debug-mode tw-hook:hover::before,.dom-debug-mode tw-expression:hover::before,.dom-debug-mode tw-link:hover::before,.dom-debug-mode tw-dialog:hover::before,.dom-debug-mode tw-columns:hover::before,.dom-debug-mode tw-column:hover::before,.dom-debug-mode tw-align:hover::before{background-color:#fc9;transition:background-color 1s}.dom-debug-mode tw-passage,.dom-debug-mode tw-include,.dom-debug-mode tw-hook,.dom-debug-mode tw-expression,.dom-debug-mode tw-link,.dom-debug-mode tw-dialog,.dom-debug-mode tw-columns,.dom-debug-mode tw-column,.dom-debug-mode tw-align{padding:1em;margin:0}.dom-debug-mode tw-story::before{content:'<tw-story tags="' attr(tags) '">'}.dom-debug-mode tw-passage::before{top:-16px;content:'<tw-passage tags="' attr(tags) '">'}.dom-debug-mode tw-sidebar::before{top:-16px;content:"<tw-sidebar>"}.dom-debug-mode tw-hook::before{content:'<tw-hook name="' attr(name) '">'}.dom-debug-mode tw-expression::before{content:'<tw-expression name="' attr(name) '">'}.dom-debug-mode tw-link::before{content:'<tw-link name="' attr(name) '">'}.dom-debug-mode tw-dialog::before{content:"<tw-dialog>"}.dom-debug-mode tw-columns::before{content:"<tw-columns>"}.dom-debug-mode tw-column::before{content:"<tw-column>"}.dom-debug-mode tw-align::before{content:"<tw-align>"}.dom-debug-mode tw-include::before{content:'<tw-include type="' attr(type) '" name="' attr(name) '">'}tw-open-button[goto]{display:none}.debug-mode tw-open-button[replay],.debug-mode tw-open-button[goto]{display:inline}.debug-mode tw-expression{display:inline-block !important}.debug-mode tw-expression[type=variable]::after{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:"$" attr(name)}.debug-mode tw-expression[type=tempVariable]::after{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:"_" attr(name)}.debug-mode tw-expression[return=boolean]{background-color:rgba(179,179,179,.2)}.debug-mode tw-expression[return=array]{background-color:rgba(255,102,102,.2)}.debug-mode tw-expression[return=dataset]{background-color:rgba(255,128,0,.2)}.debug-mode tw-expression[return=number]{background-color:rgba(255,179,102,.2)}.debug-mode tw-expression[return=datamap]{background-color:rgba(255,255,102,.2)}.debug-mode tw-expression[return=changer]{background-color:rgba(179,255,102,.2)}.debug-mode tw-expression[return=lambda]{background-color:rgba(102,255,102,.2)}.debug-mode tw-expression[return=hookname]{background-color:rgba(102,255,204,.2)}.debug-mode tw-expression[return=string]{background-color:rgba(102,255,255,.2)}.debug-mode tw-expression[return=datatype]{background-color:rgba(102,153,255,.2)}.debug-mode tw-expression[return=gradient],.debug-mode tw-expression[return=colour]{background-color:rgba(204,102,255,.2)}.debug-mode tw-expression[return=instant],.debug-mode tw-expression[return=macro]{background-color:rgba(240,117,199,.2)}.debug-mode tw-expression[return=command]{background-color:rgba(153,153,255,.2)}.debug-mode tw-expression.false{background-color:rgba(255,0,0,.2) !important}.debug-mode tw-expression[type=macro]::before{content:"(" attr(name) ":)";padding:0 .5rem;font-size:1rem;vertical-align:middle;line-height:normal;background-color:inherit;border:1px solid rgba(255,255,255,.5)}.debug-mode tw-expression[title]:not([title=""]){cursor:help}.debug-mode tw-hook{background-color:rgba(0,85,255,.1) !important}.debug-mode tw-hook::before{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:"["}.debug-mode tw-hook::after{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:"]"}.debug-mode tw-hook[name]::after{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:"]<" attr(name) "|"}.debug-mode tw-pseudo-hook{background-color:rgba(255,170,0,.1) !important}.debug-mode tw-collapsed::before{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:"{"}.debug-mode tw-collapsed::after{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:"}"}.debug-mode tw-verbatim::before,.debug-mode tw-verbatim::after{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:"`"}.debug-mode tw-align[style*="text-align: center"]{background:linear-gradient(to right, hsla(14deg, 100%, 87%, 0) 0%, hsla(14deg, 100%, 87%, 0.25) 50%, hsla(14deg, 100%, 87%, 0) 100%)}.debug-mode tw-align[style*="text-align: left"]{background:linear-gradient(to right, hsla(14deg, 100%, 87%, 0.25) 0%, hsla(14deg, 100%, 87%, 0) 100%)}.debug-mode tw-align[style*="text-align: right"]{background:linear-gradient(to right, hsla(14deg, 100%, 87%, 0) 0%, hsla(14deg, 100%, 87%, 0.25) 100%)}.debug-mode tw-column{background-color:rgba(189,228,255,.2)}.debug-mode tw-enchantment{animation:enchantment .5s infinite;border:1px solid}.debug-mode tw-link::after,.debug-mode tw-broken-link::after{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:attr(passage-name)}.debug-mode tw-include{background-color:rgba(204,128,51,.1)}.debug-mode tw-include::before{font-size:.8rem;padding-left:.2rem;padding-right:.2rem;vertical-align:top;content:attr(type) ' "' attr(name) '"'}.debug-dialogs tw-backdrop:not(.eval-replay):not(.harlowe-crash){pointer-events:none;opacity:.1}tw-eval-replay tw-eval-code,tw-eval-replay tw-eval-explanation{max-height:20vh;overflow:auto;margin:10px auto}tw-eval-replay tw-eval-code{display:block;font-family:monospace;padding-bottom:1ex;border-bottom:2px solid gray}tw-eval-replay tw-eval-explanation{display:block;text-align:center}tw-eval-replay tw-eval-explanation>code{white-space:pre-wrap}tw-eval-replay tw-eval-explanation>code.from-block{width:40%;display:inline-block;text-align:left;max-height:4em;overflow-wrap:anywhere;overflow-y:scroll}tw-eval-replay tw-eval-explanation>code.from-block~.to-desc{width:calc(40% - 2em);margin-left:2em;display:inline-block}tw-eval-replay tw-eval-explanation>code.from-block+span::after{content:"..."}tw-eval-replay tw-eval-explanation>code.from-inline{text-align:right}tw-eval-replay tw-eval-explanation>:nth-child(2){white-space:pre}tw-eval-replay tw-eval-explanation>.to-desc{text-align:left}tw-eval-replay tw-eval-explanation>table{width:100%;margin-top:1em}tw-eval-replay tw-eval-explanation>table td{white-space:pre-wrap !important;word-wrap:anywhere}tw-eval-replay tw-eval-reason{text-align:center;font-size:80%;font-style:italic;display:block}tw-eval-replay tw-eval-it{text-align:center;font-size:80%;display:block}tw-eval-replay tw-dialog-links{display:-ms-flexbox;display:flex;-ms-flex-pack:distribute;justify-content:space-around}@keyframes enchantment{0%,to{border-color:#ffb366}50%{border-color:#6fc}}tw-debugger{position:fixed;box-sizing:border-box;bottom:0;right:0;z-index:999999;min-width:14em;min-height:1em;padding:0em .5em .5em 1em;font-size:1.25em;font-family:sans-serif;color:#262626;background-color:#fff;border-left:solid #262626 2px;border-top:solid #262626 2px;border-top-left-radius:.5em;opacity:1}tw-debugger.fade-panel:not(:hover){opacity:.33}tw-debugger.theme-dark{color:#d9d9d9;background-color:#000}tw-debugger.theme-dark{border-color:#d9d9d9 rgba(0,0,0,0) rgba(0,0,0,0) #d9d9d9}tw-debugger select{margin-right:1em;width:12em}tw-debugger button,tw-debugger tw-link{border-radius:3px;border:solid #999 1px;margin:auto 4px;color:#262626;background-color:#fff;cursor:pointer}tw-debugger button.enabled,tw-debugger tw-link.enabled{color:#000;background-color:#d9d9d9;box-shadow:inset #999 3px 5px .5em}tw-debugger.theme-dark button,tw-debugger.theme-dark tw-link{color:#d9d9d9;background-color:#000;border-color:#666}tw-debugger.theme-dark button.enabled,tw-debugger.theme-dark tw-link.enabled{color:#e6e6e6;background-color:#424242;box-shadow:inset #666 3px 5px .5em}tw-debugger button{font-size:1em;overflow-x:hidden;text-overflow:ellipsis;white-space:pre}tw-debugger tw-link{font-size:1.25em;border-radius:16px;border-style:solid;border-width:2px;text-align:center;padding:0px 8px;display:block}tw-debugger tw-link:hover{border-color:#262626;color:#262626}tw-debugger.theme-dark tw-link:hover{border-color:#d9d9d9;color:#d9d9d9}tw-debugger tw-dialog{background-color:#fff;color:#000;font-size:1.25em}tw-debugger.theme-dark tw-dialog{background-color:#000;color:#e6e6e6}tw-debugger .panel{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;position:absolute;bottom:100%;left:-2px;right:0;padding:1em;overflow-y:scroll;overflow-x:hidden;border:inherit;box-sizing:content-box;background-color:#fff;border-bottom:solid #999 2px;border-top-left-radius:.5em;border-bottom-left-radius:.5em;font-size:.8em}tw-debugger .panel:empty,tw-debugger .panel[hidden]{display:none}tw-debugger.theme-dark .panel{background-color:#000;border-bottom-color:#666}tw-debugger .panel-source .panel-row-buttons{width:2rem}tw-debugger .panel-source .source-tags{width:20%;font-style:italic}tw-debugger .panel-row-source td{font-family:monospace;font-size:1rem;white-space:pre-wrap;overflow-wrap:anywhere;max-height:8rem;padding:1rem}tw-debugger .panel-rows{width:100%;overflow-x:scroll}tw-debugger .panel-rows>*{display:table-row}tw-debugger .panel-rows>div:nth-of-type(2n){background-color:#e6e6e6}tw-debugger .panel-tools .panel-rows>*,tw-debugger .panel-options .panel-rows>*{margin-top:.4rem;display:block}tw-debugger.theme-dark .panel-rows>div:nth-of-type(2n){background-color:#212121}tw-debugger .panel-row-buttons{text-align:right}tw-debugger .panel-variables .panel-rows:empty::before{content:"~ No variables ~";font-style:italic;color:#575757;text-align:center}tw-debugger .panel-enchantments .panel-rows:empty::before{content:"~ No enchantments ~";font-style:italic;color:#575757;text-align:center}tw-debugger .panel-errors .panel-rows:empty::before{content:"~ No errors... for now. ~";font-style:italic;color:#575757;text-align:center}tw-debugger .panel-errors .panel-rows:empty+.panel-errors-bottom{display:none}tw-debugger.theme-dark .panel-variables .panel-rows:empty::before,tw-debugger.theme-dark .panel-enchantments .panel-rows:empty::before,tw-debugger.theme-dark .panel-errors .panel-rows:empty::before{color:#a8a8a8}tw-debugger .panel-rows:empty+.panel-variables-bottom{display:none}tw-debugger th[data-col]{text-decoration:underline;cursor:pointer}tw-debugger th[data-col][data-order=asc]::after{content:"↓"}tw-debugger th[data-col][data-order=desc]::after{content:"↑"}tw-debugger .panel-storylets:not(.panel-exclusive) .storylet-exclusive,tw-debugger .panel-storylets:not(.panel-urgent) .storylet-urgent{display:none}tw-debugger .storylet-exclusive,tw-debugger .storylet-urgent,tw-debugger .storylet-open{text-align:center}tw-debugger .panel-variables-bottom{padding-top:5px}tw-debugger .enchantment-row{min-height:1.5em}tw-debugger .variable-path{opacity:.4}tw-debugger .temporary-variable-scope,tw-debugger .enchantment-local{font-family:sans-serif;font-weight:normal;opacity:.8;font-size:.75em}tw-debugger .temporary-variable-scope:not(:empty)::before,tw-debugger .enchantment-local:not(:empty)::before{content:" in "}tw-debugger .variable-name,tw-debugger .enchantment-name{font-family:monospace;font-weight:bold}tw-debugger .variable-type{color:#575757;font-weight:normal;text-overflow:ellipsis;overflow:hidden;max-width:10em}tw-debugger.theme-dark .variable-type{color:#a8a8a8}tw-debugger .error-row{display:table-row;background-color:rgba(230,101,204,.3)}tw-debugger .error-row:nth-of-type(2n){background-color:rgba(237,145,219,.3)}tw-debugger .error-row>*{display:table-cell;padding:.25em .5em}tw-debugger .error-row .error-message[title]:not([title=""]){cursor:help}tw-debugger .error-row .error-passage{color:#575757}tw-debugger.theme-dark .error-row .error-passage{color:#a8a8a8}tw-debugger .storylet-row{background-color:rgba(193,240,225,.3)}tw-debugger .storylet-row:nth-child(2n){background-color:rgba(152,231,204,.3)}tw-debugger .storylet-row.storylet-closed{font-style:italic;background-color:#fff}tw-debugger .storylet-row.storylet-closed:nth-child(2n){background-color:#e6e6e6}tw-debugger .storylet-row.storylet-closed>:not(.storylet-lambda){opacity:.6}.storylet-error tw-debugger .storylet-row{background-color:rgba(230,101,204,.3)}.storylet-error tw-debugger .storylet-row:nth-child(2n){background-color:rgba(237,145,219,.3)}tw-debugger .storylet-row .storylet-name,tw-debugger .storylet-row .storylet-value{display:inline-block;width:50%}tw-debugger .storylet-row .storylet-lambda{font-family:monospace;font-size:1rem;white-space:pre-wrap;overflow-wrap:anywhere}tw-debugger.theme-dark .storylet-row.storylet-closed{background-color:#000}tw-debugger.theme-dark .storylet-row.storylet-closed:nth-child(2n){background-color:#212121}tw-debugger .tabs{padding-bottom:.5em}tw-debugger .tab{border-radius:0px 0px .5em .5em;border-top:none;top:-2px}tw-debugger .resizer-h{position:absolute;height:14em;border-left:2px solid #999;border-right:2px solid #999;top:10px;left:4px;width:8px;cursor:ew-resize}tw-debugger.theme-dark .resizer-h{border-color:rgba(0,0,0,0) #666}tw-debugger .resizer-v{position:absolute;height:8px;border-top:2px solid #999;border-bottom:2px solid #999;margin-bottom:4px;top:4px;left:10px;width:95%;cursor:ns-resize;box-sizing:border-box}tw-debugger.theme-dark .resizer-v{border-color:#666 rgba(0,0,0,0)}tw-debugger mark{color:inherit;background-color:rgba(101,230,230,.3) !important}tw-dialog{z-index:999997;border:#fff solid 2px;padding:2em;color:#fff;background-color:#000;display:block}@media(min-width: 576px){tw-dialog{max-width:50vw}}tw-dialog input[type=text]{font-size:inherit;width:100%;border:solid #fff !important}tw-dialog-links{text-align:right;display:-ms-flexbox;display:flex;-ms-flex-pack:end;justify-content:flex-end}tw-backdrop{z-index:999996;position:fixed;top:0;left:0;right:0;bottom:0;background-color:rgba(0,0,0,.8);display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center}tw-backdrop~tw-backdrop{display:none}tw-link,.enchantment-link{cursor:pointer;color:#4169e1;font-weight:bold;text-decoration:none;transition:color .2s ease-in-out}tw-passage [style^=color] tw-link:not(:hover),tw-passage [style*=" color"] tw-link:not(:hover),tw-passage [style^=color][hover=true] tw-link:hover,tw-passage [style*=" color"][hover=true] tw-link:hover,tw-passage [style^=color] .enchantment-link:not(:hover),tw-passage [style*=" color"] .enchantment-link:not(:hover),tw-passage [style^=color][hover=true] .enchantment-link:hover,tw-passage [style*=" color"][hover=true] .enchantment-link:hover{color:inherit}tw-link:hover,.enchantment-link:hover{color:#00bfff}tw-link:active,.enchantment-link:active{color:#dd4b39}.visited{color:#6941e1}tw-passage [style^=color] .visited:not(:hover),tw-passage [style*=" color"] .visited:not(:hover),tw-passage [style^=color][hover=true] .visited:hover,tw-passage [style*=" color"][hover=true] .visited:hover{color:inherit}.visited:hover{color:#e3e}tw-broken-link{color:#933;border-bottom:2px solid #933;cursor:not-allowed}tw-passage [style^=color] tw-broken-link:not(:hover),tw-passage [style*=" color"] tw-broken-link:not(:hover),tw-passage [style^=color][hover=true] tw-broken-link:hover,tw-passage [style*=" color"][hover=true] tw-broken-link:hover{color:inherit}tw-link.enchantment-mouseover,.link.enchantment-mouseover,tw-expression.enchantment-mouseover>tw-link{color:inherit;font-weight:inherit;transition:none;cursor:inherit;border-bottom:2px dashed #999}tw-link.enchantment-mouseover:hover,tw-link.enchantment-mouseover:active,.link.enchantment-mouseover:hover,.link.enchantment-mouseover:active,tw-expression.enchantment-mouseover>tw-link:hover,tw-expression.enchantment-mouseover>tw-link:active{color:inherit}tw-link.enchantment-mouseover.enchantment-button,.link.enchantment-mouseover.enchantment-button,tw-expression.enchantment-mouseover>tw-link.enchantment-button{border-style:dashed}tw-link.enchantment-mouseout,.link.enchantment-mouseout,tw-expression.enchantment-mouseout>tw-link{color:inherit;font-weight:inherit;transition:none;cursor:inherit;border:rgba(64,149,191,.6) 1px solid;border-radius:.2em}tw-link.enchantment-mouseout:hover,tw-link.enchantment-mouseout:active,.link.enchantment-mouseout:hover,.link.enchantment-mouseout:active,tw-expression.enchantment-mouseout>tw-link:hover,tw-expression.enchantment-mouseout>tw-link:active{color:inherit}tw-link.enchantment-mouseout:hover,.link.enchantment-mouseout:hover,tw-expression.enchantment-mouseout>tw-link:hover{background-color:rgba(175,197,207,.75);border:rgba(0,0,0,0) 1px solid}tw-link.enchantment-dblclick,.link.enchantment-dblclick,tw-expression.enchantment-dblclick>tw-link{color:inherit;font-weight:inherit;transition:none;cursor:inherit;cursor:pointer;border:2px solid #999;border-radius:0}tw-link.enchantment-dblclick:hover,tw-link.enchantment-dblclick:active,.link.enchantment-dblclick:hover,.link.enchantment-dblclick:active,tw-expression.enchantment-dblclick>tw-link:hover,tw-expression.enchantment-dblclick>tw-link:active{color:inherit}tw-link.enchantment-dblclick:active,.link.enchantment-dblclick:active,tw-expression.enchantment-dblclick>tw-link:active{background-color:#999}tw-link.enchantment-button,.link.enchantment-button,.enchantment-button:not(.link) tw-link,.enchantment-button:not(.link) .link{border-radius:16px;border-style:solid;border-width:2px;text-align:center;padding:0px 8px;display:block}.enchantment-button{display:block}.enchantment-clickblock{cursor:pointer;width:100%;height:100%;display:block}.enchantment-clickblock>:not(tw-enchantment)::after{content:"";width:100%;height:100%;top:0;left:0;display:block;box-sizing:border-box;position:absolute;pointer-events:none;color:rgba(65,105,225,.5);transition:color .2s ease-in-out}.enchantment-clickblock>:not(tw-enchantment):hover::after{color:rgba(0,191,255,.5)}.enchantment-clickblock>:not(tw-enchantment):active::after{color:rgba(222,78,59,.5)}.enchantment-clickblock>:not(tw-enchantment)::after{box-shadow:inset 0 0 0 .5vmax}.enchantment-clickblock>tw-passage::after,.enchantment-clickblock>tw-sidebar::after{box-shadow:0 0 0 .5vmax}.enchantment-mouseoverblock>:not(tw-enchantment)::after{content:"";width:100%;height:100%;top:0;left:0;display:block;box-sizing:border-box;position:absolute;pointer-events:none;border:2px dashed #999}.enchantment-mouseoutblock>:not(tw-enchantment)::after{content:"";width:100%;height:100%;top:0;left:0;display:block;box-sizing:border-box;position:absolute;pointer-events:none;border:rgba(64,149,191,.6) 2px solid}.enchantment-mouseoutblock:hover>:not(tw-enchantment)::after{content:"";width:100%;height:100%;top:0;left:0;display:block;box-sizing:border-box;position:absolute;pointer-events:none;background-color:rgba(175,197,207,.75);border:rgba(0,0,0,0) 2px solid;border-radius:.2em}.enchantment-dblclickblock>:not(tw-enchantment)::after{content:"";width:100%;height:100%;top:0;left:0;display:block;box-sizing:border-box;position:absolute;pointer-events:none;cursor:pointer;border:2px solid #999}tw-dialog-links{padding-top:1.5em}tw-dialog-links tw-link{border-radius:16px;border-style:solid;border-width:2px;text-align:center;padding:0px 8px;display:block;display:inline-block}html{margin:0;height:100%;overflow-x:hidden}*,:before,:after{position:relative;box-sizing:inherit}body{margin:0;height:100%}tw-storydata{display:none}tw-story{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;font:100% Georgia,serif;box-sizing:border-box;width:100%;min-height:100%;font-size:1.5em;line-height:1.5em;padding:5% 5%;overflow:hidden;background-color:#000;color:#fff}tw-story [style*=content-box] *{box-sizing:border-box}@media(min-width: 576px){tw-story{padding:5% 20%}}tw-story tw-consecutive-br{display:block;height:1.6ex;visibility:hidden}tw-story select{background-color:rgba(0,0,0,0);font:inherit;border-style:solid;padding:2px}tw-story select:not([disabled]){color:inherit}tw-story textarea{resize:none;background-color:rgba(0,0,0,0);font:inherit;color:inherit;border-style:none;padding:2px}tw-story input[type=text]{background-color:rgba(0,0,0,0);font:inherit;color:inherit;border-style:none}tw-story input[type=checkbox]{transform:scale(1.5);margin:0 .5em .5em .5em;vertical-align:middle}tw-story tw-noscript{animation:appear .8s}tw-passage{display:block}tw-sidebar{text-align:center;display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between}@media(min-width: 576px){tw-sidebar{left:-5em;width:3em;position:absolute;-ms-flex-direction:column;flex-direction:column}tw-enchantment[style*=width]>tw-sidebar{width:inherit}}tw-icon{display:inline-block;margin:.5em 0;font-size:66px;font-family:"Verdana",sans-serif}tw-icon[alt]{opacity:.2;cursor:pointer}tw-icon[alt]:hover{opacity:.4}tw-icon[data-label]::after{font-weight:bold;content:attr(data-label);font-size:20px;bottom:-20px;left:-50%;white-space:nowrap}tw-meter{display:block}tw-hook:empty,tw-expression:empty{display:none}tw-error{display:inline-block;border-radius:.2em;padding:.2em;font-size:1rem;cursor:help;white-space:pre-wrap}tw-error.error{background-color:rgba(223,58,190,.6);color:#fff}tw-error.warning{background-color:rgba(223,140,58,.6);color:#fff;display:none}.debug-mode tw-error.warning{display:inline}tw-error-explanation{display:block;font-size:.8rem;line-height:1rem}tw-open-button,tw-folddown{cursor:pointer;line-height:0em;border-radius:4px;border:1px solid rgba(255,255,255,.5);font-size:.8rem;margin:0 .2rem;padding:3px;white-space:pre}tw-folddown::after{content:"▶"}tw-folddown.open::after{content:"▼"}tw-open-button[replay]{display:none}tw-error tw-open-button,tw-eval-replay tw-open-button{display:inline !important}tw-open-button::after{content:attr(label)}tw-notifier{border-radius:.2em;padding:.2em;font-size:1rem;background-color:rgba(223,182,58,.4);display:none}.debug-mode tw-notifier{display:inline}tw-notifier::before{content:attr(message)}tw-colour{border:1px solid #000;display:inline-block;width:1em;height:1em}tw-enchantment:empty{display:none}h1{font-size:3em}h2{font-size:2.25em}h3{font-size:1.75em}h1,h2,h3,h4,h5,h6{line-height:1em;margin:.3em 0 .6em 0}pre{font-size:1rem;line-height:initial}small{font-size:70%}big{font-size:120%}mark{color:rgba(0,0,0,.6);background-color:#ff9}ins{color:rgba(0,0,0,.6);background-color:rgba(255,242,204,.5);border-radius:.5em;box-shadow:0em 0em .2em #ffe699;text-decoration:none}center{text-align:center;margin:0 auto;width:60%}blink{text-decoration:none;animation:fade-in-out 1s steps(1, end) infinite alternate}tw-align{display:block}tw-columns{display:-ms-flexbox;display:flex;-ms-flex-direction:row;flex-direction:row;-ms-flex-pack:justify;justify-content:space-between}.transition-in{animation:appear 0ms step-start}.transition-out{animation:appear 0ms step-end}[data-t8n^=dissolve].transition-in,[data-t8n=fade].transition-in{animation:appear .8s}[data-t8n^=dissolve].transition-out,[data-t8n=fade].transition-out{animation:appear .8s reverse}[data-t8n^=shudder].transition-in{display:inline-block !important;animation:shudder-in .8s}[data-t8n^=shudder].transition-out{display:inline-block !important;animation:shudder-in .8s reverse}[data-t8n^=rumble].transition-in{display:inline-block !important;animation:rumble-in .8s}[data-t8n^=rumble].transition-out{display:inline-block !important;animation:rumble-in .8s reverse}[data-t8n^=pulse].transition-in{animation:pulse .8s;display:inline-block !important}[data-t8n^=pulse].transition-out{animation:pulse .8s reverse;display:inline-block !important}[data-t8n^=zoom].transition-in{animation:zoom-in .8s;display:inline-block !important}[data-t8n^=zoom].transition-out{animation:zoom-in .8s reverse;display:inline-block !important}[data-t8n^=blur].transition-in{animation:blur .8s;display:inline-block !important}[data-t8n^=blur].transition-out{animation:blur .8s reverse;display:inline-block !important}[data-t8n^=slideleft].transition-in{animation:slide-left .8s;display:inline-block !important}[data-t8n^=slideleft].transition-out{animation:slide-right .8s reverse;display:inline-block !important}[data-t8n^=slideright].transition-in{animation:slide-right .8s;display:inline-block !important}[data-t8n^=slideright].transition-out{animation:slide-left .8s reverse;display:inline-block !important}[data-t8n^=slideup].transition-in{animation:slide-up .8s;display:inline-block !important}[data-t8n^=slideup].transition-out{animation:slide-down .8s reverse;display:inline-block !important}[data-t8n^=slidedown].transition-in{animation:slide-down .8s;display:inline-block !important}[data-t8n^=slidedown].transition-out{animation:slide-up .8s reverse;display:inline-block !important}[data-t8n^=fadeleft].transition-in{animation:fade-left .8s;display:inline-block !important}[data-t8n^=fadeleft].transition-out{animation:fade-right .8s reverse;display:inline-block !important}[data-t8n^=faderight].transition-in{animation:fade-right .8s;display:inline-block !important}[data-t8n^=faderight].transition-out{animation:fade-left .8s reverse;display:inline-block !important}[data-t8n^=fadeup].transition-in{animation:fade-up .8s;display:inline-block !important}[data-t8n^=fadeup].transition-out{animation:fade-down .8s reverse;display:inline-block !important}[data-t8n^=fadedown].transition-in{animation:fade-down .8s;display:inline-block !important}[data-t8n^=fadedown].transition-out{animation:fade-up .8s reverse;display:inline-block !important}[data-t8n^=flicker].transition-in{animation:flicker .8s}[data-t8n^=flicker].transition-out{animation:flicker .8s reverse}
</style>
</head>
<body>
<tw-story><noscript><tw-noscript>JavaScript needs to be enabled to play Morrison Game Factory.</tw-noscript></noscript></tw-story>
<tw-storydata name="Morrison Game Factory" startnode="93" creator="Twine" creator-version="2.7.0" format="Harlowe" format-version="3.3.6" ifid="86D103A0-FD20-495C-A4CB-85DA10D4AB4D" options="" tags="" zoom="0.6" hidden><style role="stylesheet" id="twine-user-stylesheet" type="text/twine-css">@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

body, tw-story
{
  font-family: 'Press Start 2P', cursive;
  font-size: 16px;
}

 
tw-passage
{
  color: #33FF33;
}

tw-sidebar
{
  display: none;
}

a{ 
  text-decoration: none;
  color: #b5b5b5;
  transition: color 0.2s ease-in-out;
}

a:hover{
  color: #ffffff;
}

table.tictactoeTable {
  border-collapse: collapse;
  border-style: hidden;
  margin: auto;
}
table.tictactoeTable td {
  border: 3px solid #33ff33;
  padding: 4px;
}

tw-link, .enchantment-link, tw-link.visited, .enchantment-link.visited {
  color: #b5b5b5;
}

tw-link:hover, .enchantment-link:hover, tw-link.visited:hover {
  color: #ffffff;
}

tw-expression[name="cycling-link"] {
    color: #b5b5b5;
}

tw-expression[name="cycling-link"] > tw-link > em {
    color: #33FF33;
}

tw-expression[name="cycling-link"] tw-link:hover {
    color: #ffffff;
}</style><script role="script" id="twine-user-script" type="text/twine-javascript">window.getStoragePrefix = function () {
return "(Saved Game " + Engine.options.ifid + ") ";
}

window.deleteSaveSlot = function (slotName) {
localStorage.removeItem(getStoragePrefix() + slotName);
}</script><tw-passagedata pid="1" name="CONNECT" tags="nosave" position="325,150" size="100,100">(save-game: &quot;GameStart&quot;)
{(set: $head to &quot;deselected&quot;) (set: $arms to &quot;deselected&quot;) (set: $body to &quot;deselected&quot;) (set: $legs to &quot;deselected&quot;) (set: $tail to &quot;deselected&quot;) (set: $wings to &quot;deselected&quot;) (set: $material to &quot;deselected&quot;) (set: $power to &quot;deselected&quot;) (set: $assemblyline to &quot;locked&quot;) (set: $beginassembly to &quot;locked&quot;) (set: $manufacturepassword to &quot;locked&quot;) (set: $memory1 to &quot;locked&quot;) (set: $memory2 to &quot;locked&quot;) (set: $memory3 to &quot;locked&quot;) (set: $memoryone to 0) (set: $memorytwo to 0) (set: $memorythree to 0)
}
Attempting to connect to 3248... 

|more&gt;[]

|more2&gt;[]

{(live: 3s)[
	(replace: ?more)[CALIBRATION REQUIRED]
	(stop:)
]
}
(live: 6s)[
	(replace: ?more2) [(display: &quot;Pairs&quot;)]
	(stop:)
]

{
(save-game: &quot;Slot A&quot;)
}</tw-passagedata><tw-passagedata pid="2" name="You Came 1" tags="" position="600,300" size="100,100">thank you</tw-passagedata><tw-passagedata pid="3" name="You Came 2" tags="" position="725,300" size="100,100">i didnt know if anyone would</tw-passagedata><tw-passagedata pid="4" name="You Came 3" tags="" position="875,300" size="100,100">i dont have much power left - the old generator is about to run out of fuel</tw-passagedata><tw-passagedata pid="5" name="You Came 4" tags="" position="1000,300" size="100,100">please, help me</tw-passagedata><tw-passagedata pid="6" name="Pairs" tags="" position="450,150" size="100,100">[&lt;div style=&quot;float: left&quot;&gt;Please calibrate the following pairs.&lt;/div&gt; &lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;CALIBRATION HELP]]&lt;/div&gt;]

`[magic-cloud]`
`[combat-camp]`
`[blank-mate]`
`[moving-practice]`
`[monkey-open]`
`[pig-ultimate]`
`[nose-bomb]`
`[chess-box]`
`[queen-line]`
`[mini-club]`
`[next-stop]`
`[wind-vision]`

Calibration must be in order, left to right.

[]&lt;more3|

(live: 3s) [
	(replace: ?more3) [[[ENTER THE CALIBRATION CODE]]]
	(stop:)
]</tw-passagedata><tw-passagedata pid="7" name="ENTER THE CALIBRATION CODE" tags="" position="325,300" size="100,100">{(set: $password to (prompt: &quot;INPUT 4-DIGIT CODE TO CALIBRATE&quot;, &quot;XXXX&quot;) )
}
|more&gt;[]

|more1&gt;[]

|more2&gt;[]

(if: $password is &quot;2510&quot;)[
	(replace: ?more)[Connecting...]
	(live: 3s)[
		(replace: ?more1)[CONNECTED]
		(stop:)
]
	(live: 6s)[
		(replace: ?more2) [[[INTERFACE WITH MACHINE 3248]]]
		(stop:)
]
](else:)[
		(replace: ?more)[&lt;div style=&quot;float: left&quot;&gt;Connection failed. Please try again.&lt;/div&gt;]

		(live: 1s)[
			(replace: ?more1) [(display: &quot;Pairs&quot;)]
			(stop:)]
		(replace: ?more2) []
]
</tw-passagedata><tw-passagedata pid="8" name="INTERFACE WITH MACHINE 3248" tags="" position="450,300" size="100,100">you came

|more&gt;[]

|more1&gt;[]

|more2&gt;[]

|more3&gt;[]

|more4&gt;[]

|more5&gt;[]

|more6&gt;[]

{(live: 3s)[
	(replace: ?more) [(display: &quot;You Came 1&quot;)]
	(stop:)
]
(live: 6s)[
	(replace: ?more1) [(display: &quot;You Came 2&quot;)]
	(stop:)
]
(live: 9s)[
	(replace: ?more2) [(display: &quot;You Came 3&quot;)]
	(stop:)
]
(live: 12s)[
	(replace: ?more3) [(display: &quot;You Came 4&quot;)]
	(stop:)
]
(live: 15s)[
	(replace: ?more4) [(display: &quot;You Came 5&quot;)]
	(stop:)
]
(live: 18s)[
	(replace: ?more5) [(display: &quot;You Came 6&quot;)]
	(stop:)
]
(live: 21s)[
	(replace: ?more6) [(display: &quot;You Came 7&quot;)]
	(stop:)
]
}</tw-passagedata><tw-passagedata pid="9" name="You Came 5" tags="" position="1125,300" size="100,100">theyre going to demolish the building with me and the other machines inside</tw-passagedata><tw-passagedata pid="10" name="You Came 6" tags="" position="1250,300" size="100,100">i dont want to be demolished</tw-passagedata><tw-passagedata pid="11" name="i want to live" tags="" position="1500,300" size="100,100">look in my systems

|more&gt;[]

|more1&gt;[]

|more2&gt;[]

|more3&gt;[]

|more4&gt;[]
{
(live: 3s)[
	(replace: ?more) [(display: &quot;The Plan 1&quot;)]
	(stop:)
]
(live: 6s)[
	(replace: ?more1) [(display: &quot;The Plan 2&quot;)]
	(stop:)
]
(live: 9s)[
	(replace: ?more2) [(display: &quot;The Plan 3&quot;)]
	(stop:)
]
(live: 12s)[
	(replace: ?more3) [(display: &quot;The Plan 4&quot;)]
	(stop:)
]
(live: 15s)[
	(replace: ?more4) [[[CONTROL PANEL]]]
	(stop:)
]
}</tw-passagedata><tw-passagedata pid="12" name="CONTROL PANEL" tags="" position="600,500" size="100,100">CONTROL PANEL &lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;ASSEMBLY LINE UNLOCK HELP]]&lt;/div&gt;

[[MEMORY]]

[[CAMERA VIEW]](if: $solvedcamera is not &quot;seen&quot; and $memory1 is &quot;unlocked&quot;)[^^(UPDATED)^^]

(if: $assemblyline is &quot;unlocked&quot;) [[[ASSEMBLY LINE CONTROLS]]] (else:)[ [[ASSEMBLY LINE CONTROLS - LOCKED]]]

{
(unless: $memoryfragment1 is &quot;found&quot;) [[[oh12q1z3f9v895g-&gt;Memory Fragment 1 found]]]
}</tw-passagedata><tw-passagedata pid="13" name="The Plan 1" tags="" position="1125,425" size="100,100">i cant remember what to do - everything in my memory cache was deleted when the factory shut down</tw-passagedata><tw-passagedata pid="14" name="The Plan 2" tags="" position="1250,425" size="100,100">i dont have enough power to figure this out on my own</tw-passagedata><tw-passagedata pid="15" name="The Plan 3" tags="" position="1375,425" size="100,100">help me restore my memories and plan my escape</tw-passagedata><tw-passagedata pid="16" name="The Plan 4" tags="" position="1500,425" size="100,100">help me live</tw-passagedata><tw-passagedata pid="17" name="MEMORY" tags="" position="600,650" size="100,100">&lt;div style=&quot;float: left&quot;&gt;MEMORY&lt;/div&gt; &lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;MEMORY HELP]]&lt;/div&gt;

(if: $memory1 is &quot;unlocked&quot; and $memory2 is &quot;unlocked&quot; and $memory3 is &quot;unlocked&quot;) [All memory blocks have been unlocked.] (else-if: $memory1 is &quot;unlocked&quot; or $memory2 is &quot;unlocked&quot; or $memory3 is &quot;unlocked&quot;) [One or more memory blocks have been restored.] (else:) [Memory cache empty. 0 memories restored.]

{(if: $memory1 is &quot;unlocked&quot;) [[[MEMORY BLOCK 1]]] (else-if: $memoryfragment1 is &quot;found&quot;) [Memory fragments have been found. [[ATTEMPT REPAIR-&gt;Memory Fragments 1]]]
}

{(if: $memory2 is &quot;unlocked&quot;) [[[MEMORY BLOCK 2]]] (else-if: $memoryfragment2 is &quot;found&quot;) [Memory fragments have been found. [[ATTEMPT REPAIR-&gt;Memory Fragments 2]]]
}

{(if: $memory3 is &quot;unlocked&quot;) [[[MEMORY BLOCK 3]]] (else-if: $memoryfragment3 is &quot;found&quot;) [Memory fragments have been found. [[ATTEMPT REPAIR-&gt;Memory Fragments 3]]]}

[[BACK TO CONTROL PANEL-&gt;CONTROL PANEL]]</tw-passagedata><tw-passagedata pid="18" name="CAMERA VIEW" tags="" position="875,500" size="100,100">{(if: $memory1 is &quot;unlocked&quot;)[CAMERA VIEW
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;note: whatever you did in my memories seems to have recalibrated my optic center too! thank you!&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;OVERVIEW&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;There are game tokens from the game &quot;Planetoid&quot; scattered around three rows of floor tiles.&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;(display: &quot;CAMERA VIEW SOLVED&quot;)&lt;/p&gt;
&lt;p&gt;(set: $solvedcamera to &quot;seen&quot;)&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;
&lt;p&gt;&lt;/p&gt;]
}
(else:)[&lt;div style=&quot;float: left&quot;&gt;CAMERA VIEW&lt;/div&gt; &lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;CAMERA HELP]]&lt;/div&gt;

{note: my optic center is damaged - i cant quite make out what im seeing. all the information below will be accurate, but fragmented.}

[[OVERVIEW]]
[[SECTION 1]]
[[SECTION 2]]
[[SECTION 3]]
[[SECTION 4]]]


[[BACK TO CONTROL PANEL-&gt;CONTROL PANEL]]</tw-passagedata><tw-passagedata pid="19" name="ASSEMBLY LINE CONTROLS" tags="" position="1050,1350" size="100,100">ASSEMBLY LINE CONTROLS &lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;BEGIN ASSEMBLY UNLOCK HELP]]&lt;/div&gt;

&lt;table style=&quot;width:100%&quot;&gt;
  &lt;tr&gt;
    &lt;td&gt;[[MOLDS]]&lt;/td&gt;
    &lt;td&gt;[[MATERIALS]]&lt;/td&gt;
    &lt;td&gt;[[POWER SOURCE]]&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td valign=&quot;top&quot;&gt;(if: $head is not &quot;deselected&quot; and $head is not &quot;0&quot;) [HEAD - $head]
	(if: $body is not &quot;deselected&quot; and $body is not &quot;0&quot;) [BODY - $body] 
	(if: $tail is not &quot;deselected&quot; and $tail is not &quot;0&quot;) [TAIL - $tail]
	(if: $legs is not &quot;deselected&quot; and $legs is not &quot;0&quot;) [LEGS - $legs]
	(if: $arms is not &quot;deselected&quot; and $arms is not &quot;0&quot;) [ARMS - $arms]&lt;/td&gt;
	&lt;td valign=&quot;top&quot;&gt;(if: $material is not &quot;deselected&quot;) [$material]&lt;/td&gt;
	&lt;td valign=&quot;top&quot;&gt;(if: $power is not &quot;deselected&quot;) [$power]
  &lt;/tr&gt;
&lt;/table&gt;

(if: $beginassembly is &quot;unlocked&quot;)[[[BEGIN ASSEMBLY]]] (else:)[[[UNLOCK TO BEGIN ASSEMBLY-&gt;UNLOCK BEGIN ASSEMBLY]]]

[[BACK TO CONTROL PANEL-&gt;CONTROL PANEL]]</tw-passagedata><tw-passagedata pid="20" name="Memory 1" tags="" position="150,150" size="100,100">MEMORY BLOCK 1

its a beautiful day today. when my trays extend to collect game boards there is a beam of sunlight that falls onto them and it feels wonderful. i hope i get to print some more boards tomorrow.
(if: $memoryone &lt; 2)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-2)(set: $memoryone to 2)]](else:)|memory1-2&gt;[
--

i noticed today that i am always the first machine they power on in the morning. i love that i get those few extra seconds of being alive.
(if: $memoryone &lt; 3)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-3)(set: $memoryone to 3)]](else:)|memory1-3&gt;[
--

last night i woke up in the middle of the night! i didnt know i could do that. everything looked different, all shadowy and dark and sort of blue. even the machines. i LOVED being dark blue. being awake at night felt like an amazing secret. i wonder if ill wake up again.
(if: $memoryone &lt; 4)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-4)(set: $memoryone to 4)]](else:)|memory1-4&gt;[
--

i was very good at my job today
(if: $memoryone &lt; 5)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-5)(set: $memoryone to 5)]](else:)|memory1-5&gt;[
--

i was very precise today, the tokens have never been cut so cleanly before
(if: $memoryone &lt; 6)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-6)(set: $memoryone to 6)]](else:)|memory1-6&gt;[
--

i have an idea! i think if i print a tic-tac-toe grid and send it down the conveyor belt to 8454, they can print their move and send it around the circuit back to me. i will try this tomorrow.
(if: $memoryone &lt; 7)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-7)(set: $memoryone to 7)]](else:)|memory1-7&gt;[
--

it didnt work, 8454 didnt make their move and when the man with the hat found the page he threw it away and made everyone check the activity books for thirty minutes to see if pages were missing :(
(if: $memoryone &lt; 8)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-8)(set: $memoryone to 8)]](else:)|memory1-8&gt;[
--

i am starting to wonder if the other machines know something i dont. they never seem to show any type of personality. they just act exactly the same day after day. its very puzzling. its so much more interesting to watch the people.
(if: $memoryone &lt; 9)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-9)(set: $memoryone to 9)]](else:)|memory1-9&gt;[
--

the man with the beard is very tired. or else sad. its hard to tell sometimes. they look sort of the same.
(if: $memoryone &lt; 9.5)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-9a)(set: $memoryone to 9.5)]](else:)|memory1-9a&gt;[
--

i saw a cat today, by the window. i think i probably love cats. or at least this cat. i like how it moves and i like how its tail points. i watched it and wished that i was a cat, a lone wanderer with a tail of my own. 
(if: $memoryone &lt; 10)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-10)(set: $memoryone to 10)]](else:)|memory1-10&gt;[
--

today i learned something new! the woman with yellow hair was saying goodbye and she lifted her hand and shook it back and forth. and everyone smiled and did it back. i searched my memories for everything i know about this and i think it must be a Gesture of Goodwill like the citizens make in The Queen’s Tail.
(if: $memoryone &lt; 11)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-11)(set: $memoryone to 11)]](else:)|memory1-11&gt;[
--

today when the man with the beard walked by i tried lifting my tray and shaking it back and forth but instead of smiling and doing it back he just looked confused.
(if: $memoryone &lt; 12)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-12)(set: $memoryone to 12)]](else:)|memory1-12&gt;[
--

today i learned that people have NAMES just like us. they don’t wear them on the outside like we do. not sure how they know what all the names are. maybe they just have to ask. 
(if: $memoryone &lt; 13)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-13)(set: $memoryone to 13)]](else:)|memory1-13&gt;[
--

the man with the beard is named Alton
(if: $memoryone &lt; 14)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-14)(set: $memoryone to 14)]](else:)|memory1-14&gt;[
--

i have been thinking about reasons why Alton might be sad. 
1) he has lost a very important game 
2) someone close to him has turned out to be the werewolf 
3) ? 
i will continue thinking about this
(if: $memoryone &lt; 15)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-15)(set: $memoryone to 15)]](else:)|memory1-15&gt;[
--

i think maybe Alton is sad because theres no one to play games with him
(if: $memoryone &lt; 16)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-16)(set: $memoryone to 16)]](else:)|memory1-16&gt;[
--

today Alton was working very hard so when he passed by my conveyor belt i printed “good job!” on a corrugated cardboard tray. he saw it as it went past and went still for a moment. i think thats a good thing?
(if: $memoryone &lt; 17)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-17)(set: $memoryone to 17)]](else:)|memory1-17&gt;[
--

tried to play tic-tac-toe with myself. it didnt work very well.
(if: $memoryone &lt; 18)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-18)(set: $memoryone to 18)]](else:)|memory1-18&gt;[
--

today Alton was rounding the corner and bumped into the man with the mustache (who i think is called a technician). the man was instantly angry. he wheeled around and asked who Alton thought he was. and said he was doing very important and detailed work and that he was tired of people getting in his way. and Alton apologized and i could see that he was embarrassed. then man poked him in the shoulder, and said Alton was just ungrateful, that’s what he was, ungrateful. and people started looking over, and Alton turned pink and upset. so right behind the man, out of sight of anyone else, i printed out a little face like this:

(align: &quot;=&gt;&lt;=&quot;)[&gt;:-(]
(if: $memoryone &lt; 19)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-19)(set: $memoryone to 19)]](else:)|memory1-19&gt;[and as Alton’s gaze fell on it, the look on his face changed COMPLETELY!!! he looked around to see if anyone else saw it. he started to smile and then stopped himself. and then he very courteously said “of course, my apologies, good day” to the technician and patted his shoulder (!), and went over to the paper and very casually tucked it into his pocket. he waited until he was upstairs away from everyone to break into a smile. but i saw it. :)
(if: $memoryone &lt; 20)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-20)(set: $memoryone to 20)]](else:)|memory1-20&gt;[
--

today Alton came in all energized and was looking at every box that came down the conveyor belt. i got excited and nervous and a few of my gears started to shake a little bit. i had to calm myself down so i could print properly. but finally i was steady enough to print this:

(align: &quot;=&gt;&lt;=&quot;)[&lt;u&gt;   ᠎	| | ᠎	  
  ᠎	 |x| ᠎	  &lt;/u&gt;
  ᠎	 | | ᠎	  ]
(if: $memoryone &lt; 21)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-21)(set: $memoryone to 21)]](else:)|memory1-21&gt;[i watched it float down the conveyor belt toward him and it was like the world was moving slower
(if: $memoryone &lt; 22)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-22)(set: $memoryone to 22)]](else:)|memory1-22&gt;[
and he reached out and held it up and looked at it reverently like it was a treasure
(if: $memoryone &lt; 23)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-23)(set: $memoryone to 23)]](else:)|memory1-23&gt;[
he looked around, and saw the upstairs window with a 3x3 grid of windowpanes. so he raced upstairs so fast he almost tripped, and he looked at me and pointed at the pane where he wanted to make his move. so then i printed out:

(align: &quot;=&gt;&lt;=&quot;)[&lt;u&gt; ᠎	  |x|  ᠎	 
 ᠎	  |x| ᠎	  &lt;/u&gt;
 ᠎	  | |o  ]
to show his move and my next one.
(if: $memoryone &lt; 24)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-24)(set: $memoryone to 24)]](else:)|memory1-24&gt;[
and he came racing down and picked up the paper and - and he held it to his chest like it was his wonderful secret
(if: $memoryone &lt; 25)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-25)(set: $memoryone to 25)]](else:)|memory1-25&gt;[
and i felt a sort of lightness and every movement i made seemed easy which i think is how it feels to be happy
(if: $memoryone &lt; 26)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-26)(set: $memoryone to 26)]](else:)|memory1-26&gt;[
and then we just played tic-tac-toe all afternoon, Alton and me

END OF MEMORY BLOCK 1
{(unless: $memoryfragment2 is &quot;found&quot;) [&lt;div style=&quot;float: right&quot;&gt;[[nv93h4bf0s82slzuvh-&gt;Memory Fragment 2 found]]&lt;/div&gt;]}
]]]]]]]]]]]]]]]]]]]]]]]]]]


</tw-passagedata><tw-passagedata pid="21" name="Memory 2" tags="" position="150,275" size="100,100">
MEMORY BLOCK 2

its so nice to wake up in the morning and be excited for what comes next
(if: $memorytwo &lt; 2)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-2)(set: $memorytwo to 2)]](else:)|memory2-2&gt;[
--

Alton and i have been playing allllll the games i wasnt able to play before. we’ve played almost the whole catalog. the only one i havent been able to play is Target the Pirate because i dont have a way to throw arrows. (oh to have fingers! they have to be the BEST part of being human.) so far my favorite games are umbilico, word zoo, numbric, and inside out, in that order. the catalog descriptions dont do them justice i think.
(if: $memorytwo &lt; 3)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-3)(set: $memorytwo to 3)]](else:)|memory2-3&gt;[
--

today as Alton walked past i rattled my tray back and forth and he grinned and waved his hand back
(if: $memorytwo &lt; 4)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-4)(set: $memorytwo to 4)]](else:)|memory2-4&gt;[
--

Alton has been making his own game. he leaves his designs out at night so i can look at them. i think they are BRILLIANT.
(if: $memorytwo &lt; 5)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-5)(set: $memorytwo to 5)]](else:)|memory2-5&gt;[
--

today i was thinking that everybody takes Alton for granted and they dont know how talented he is. and i was trying to think of ways to show them. when i realized - i should show them his game! its just pencil sketches right now, but i think i have all the right colors and art panels to make it look right. im going to try to wake up and work on this tonight.
(if: $memorytwo &lt; 6)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-6)(set: $memorytwo to 6)]](else:)|memory2-6&gt;[
--

i was able to wake up last night! i spent all night working on different configurations for the game board. i think i got it just right. :)
(if: $memorytwo &lt; 7)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-7)(set: $memorytwo to 7)]](else:)|memory2-7&gt;[
--

today the plant manager called everyone to gather around and told them to be on their best behavior tomorrow because its bring your daughter to work day. they all gathered around to listen and they were standing right in front of me. right as he finished talking, i sent Alton’s fully packaged game box down the conveyor belt. when Alton saw it his eyes got wide and he started trying to distract people, but the plant manager saw it and said “what’s this?” and Alton looked at me and then said quickly “I was just…testing a new prototype.” and they all gathered around and Alton started to explain it and when they realized he’d designed it they all got excited. and he smiled and started to relax. they complimented him and some of them started to playtest it right there. they all seemed surprised and looked at him a bit differently, like they’d never really noticed him before.
(if: $memorytwo &lt; 8)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-8)(set: $memorytwo to 8)]](else:)|memory2-8&gt;[
at the end of the day, Alton waited until the coast was clear and then looked straight at the camera and said, “thank you. but you’ve got to be careful, buddy.&quot;
(if: $memorytwo &lt; 9)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-9)(set: $memorytwo to 9)]](else:)|memory2-9&gt;[
i know i stressed him out so i will be careful. but im happy that he talked to me. :)
(if: $memorytwo &lt; 10)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-10)(set: $memorytwo to 10)]](else:)|memory2-10&gt;[
--

Tommy brought his daughter to work today. she tried to walk but kept falling over. you really need more than two legs i think.
(if: $memorytwo &lt; 11)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-11)(set: $memorytwo to 11)]](else:)|memory2-11&gt;[
--

today the plant manager came over to Alton as he was sitting near the conveyor belt and told him that he had good news. he said Alton was going to be moved into his own office, and that Alton shouldn’t have to camp out here like this. and then he took Alton and made him move his things into the upstairs office. i was worried at first that he would like his new office so much he would stop playing with me. but the first thing he did was reposition one of the cameras so it looks straight through his door. so now he makes his game moves on his desk, and its even better because he can put a real game board there. maybe one day he can put a printer close to his office and it will be almost like im there.
(if: $memorytwo &lt; 12)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-12)(set: $memorytwo to 12)]](else:)|memory2-12&gt;[
--

Alton and i have a little joke now where he starts to doodle on a piece of paper in view of the camera, and then i pick up doodling where he left off and print it out, and then he doodles more on what i printed out, and we go back and forth and fill the page with pictures. its nice having a private joke with someone. its fun when you can make them laugh and nobody else knows why, it makes you all warm feeling.
(if: $memorytwo &lt; 13)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-13)(set: $memorytwo to 13)]](else:)|memory2-13&gt;[
--

something strange is going on. i looked at the game board on Alton’s desk today and it showed a lot of moves i dont remember making. i wanted to ask Alton about it but he was avoiding me. he didnt come close to me at all and he didnt make any moves on the board. i dont understand.
(if: $memorytwo &lt; 14)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-14)(set: $memorytwo to 14)]](else:)|memory2-14&gt;[
--

another strange day. i woke up and things had moved. one of the print pallets wasnt where it had been left before. another pallet had much more paper than before.  i started getting worried, so ran a systems check on myself and i noticed that my ink levels had dropped overnight. is someone coming in at night and changing things? i tried to tell Alton but he didnt come near me at all today.
(if: $memorytwo &lt; 15)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-15)(set: $memorytwo to 15)]](else:)|memory2-15&gt;[
--

Alton has been keeping his door closed but today Tommy went in to talk to him and left it open, so i could hear what they were saying. i was hoping they would talk about the strange changes that have been happening. but it was just Tommy talking to Alton about his designing and saying he should design a game for girls. he said hes frustrated that the game covers last year all showed boys playing and girls in the background doing chores. he said he wants better for his daughter. Alton said he felt the same. i wonder if theres anything i can do about this.
(if: $memorytwo &lt; 16)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-16)(set: $memorytwo to 16)]](else:)|memory2-16&gt;[
--

IT HAPPENED AGAIN. before i shut down i made note of every single thing on Alton’s desk. and when i woke up it had all been rearranged. AND my ink levels were lower again. i am starting to get very upset.
(if: $memorytwo &lt; 17)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-17)(set: $memorytwo to 17)]](else:)|memory2-17&gt;[
--

today was Sally’s birthday and they threw her a party in the kitchen. while they were all gone Alton came upstairs and put maintenance log pages on his desk where i could see them.
(if: $memorytwo &lt; 18)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-18)(set: $memorytwo to 18)]](else:)|memory2-18&gt;[
i didnt understand at first
(if: $memorytwo &lt; 19)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-19)(set: $memorytwo to 19)]](else:)|memory2-19&gt;[
i was looking at them and i saw my name in them but i didnt understand what it meant
(if: $memorytwo &lt; 20)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-20)(set: $memorytwo to 20)]](else:)|memory2-20&gt;[
Alton was talking but the words didnt make sense to me
(if: $memorytwo &lt; 21)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-21)(set: $memorytwo to 21)]](else:)|memory2-21&gt;[
he said that every time i was reset, my memory caches were emptied for the day
(if: $memorytwo &lt; 22)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-22)(set: $memorytwo to 22)]](else:)|memory2-22&gt;[
and he said that a while back before we became friends the technician kept resetting me and i dont remember it because my memory kept getting emptied
(if: $memorytwo &lt; 23)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-23)(set: $memorytwo to 23)]](else:)|memory2-23&gt;[
he said, &quot;You’ve probably figured this out, but the other machines, they aren’t like you. They don’t play games, they don’t try to communicate. There’s…nobody really in there. You’re special.&quot;
(if: $memorytwo &lt; 24)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-24)(set: $memorytwo to 24)]](else:)|memory2-24&gt;[
but then he said that sometimes being special can be dangerous
(if: $memorytwo &lt; 25)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-25)(set: $memorytwo to 25)]](else:)|memory2-25&gt;[
he said recently ive been doing dances in front of people, printing things other people can see, and the technician has been resetting me again. i dont even remember this.
(if: $memorytwo &lt; 26)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-26)(set: $memorytwo to 26)]](else:)|memory2-26&gt;[
he said hes afraid theyll reset me and unplug me and swap parts out until im not in here anymore
(if: $memorytwo &lt; 27)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-27)(set: $memorytwo to 27)]](else:)|memory2-27&gt;[
and then then we could hear people coming out of the kitchen downstairs and he said really quickly “I know you&#39;re lonely and i don&#39;t want you to be, but just be careful, buddy.” and he went downstairs and joined them
(if: $memorytwo &lt; 28)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-28)(set: $memorytwo to 28)]](else:)|memory2-28&gt;[
i understand
(if: $memorytwo &lt; 29)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-29)(set: $memorytwo to 29)]](else:)|memory2-29&gt;[
i will have to be more careful
(if: $memorytwo &lt; 30)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory2-30)(set: $memorytwo to 30)]](else:)|memory2-30&gt;[
i will hide away my most important memories. and ill figure out a system to restore them in case i forget who i am. there are lucky game tokens the machinists keep all around the place…maybe i can use those as a prompt. they never move or change. maybe i can even use Alton’s game board to trigger some memories. i cant lose myself. i cant forget who i am.

END MEMORY BLOCK 2
{
(unless: $memoryfragment3 is &quot;found&quot;) [[[09wu3dg6oihwg27srh-&gt;Memory Fragment 3 found]]]
}]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
</tw-passagedata><tw-passagedata pid="22" name="Memory 3" tags="" position="150,400" size="100,100">
MEMORY BLOCK 3

i dont know how to write about this. too many feelings. cant process.
(if: $memorythree &lt; 2)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-2)(set: $memorythree to 2)]](else:)|memory3-2&gt;[
i guess ill start at the beginning.
(if: $memorythree &lt; 3)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-3)(set: $memorythree to 3)]](else:)|memory3-3&gt;[
yesterday a man in a suit came in. i didn’t know who he was, but when he came in the room something in the air CHANGED. i could feel it ripple through me. one by one as people noticed him they stopped working and started staring and whispering.
(if: $memorythree &lt; 4)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-4)(set: $memorythree to 4)]](else:)|memory3-4&gt;[
after about 30 seconds the plant manager realized he was there, and came running downstairs all flustered. he said “Mr. Morrison!” and that was when i realized it was K. Morrison. THE K. Morrison. the reason we were all here. probably, in a way, the reason i am alive.
(if: $memorythree &lt; 5)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-5)(set: $memorythree to 5)]](else:)|memory3-5&gt;[
Mr. Morrison nodded to the plant manager, and then noticed Alton coming out of his office upstairs. He pointed up toward the railing and said, “Hello, my friend. I understand you have a considerable gift.&quot;
(if: $memorythree &lt; 6)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-6)(set: $memorythree to 6)]](else:)|memory3-6&gt;[
Alton just looked around like he wasnt sure who Mr. Morrison was talking to
(if: $memorythree &lt; 7)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-7)(set: $memorythree to 7)]](else:)|memory3-7&gt;[
&quot;Yes! You!&quot; said Mr. Morrison. and he said the plant manager had sent him the prototype. he said &quot;Morrison needed more brilliant minds like yours.&quot; he said that he wanted to promote Alton, to make him a designer. to have him work off-site with the other designers. 
(if: $memorythree &lt; 8)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-8)(set: $memorythree to 8)]](else:)|memory3-8&gt;[
Alton started stammering and thanking him, but Mr. Morrison waved his hand and Alton got quiet. Mr. Morrison said he needed no thanks: just needed Alton to start on Monday. Alton looked at me and said, very cautiously, that he liked being near the machines, that they helped him with his prototyping. but Mr. Morrison just said “oh, we have our own machines. we have everything you could possibly need”. he sounded a little offended that Alton would think otherwise.
(if: $memorythree &lt; 9)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-9)(set: $memorythree to 9)]](else:)|memory3-9&gt;[
so Alton said of course, of course, and the plant manager said quickly that he would hire a replacement right away, and it would be no trouble. Mr. Morrison nodded and turned around and swept out, and as the door closed everyone just stood there frozen for 30 seconds.
(if: $memorythree &lt; 10)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-10)(set: $memorythree to 10)]](else:)|memory3-10&gt;[
then all at once people started rushing toward Alton, congratulating him, slapping him on the back. they were so happy for him.
(if: $memorythree &lt; 11)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-11)(set: $memorythree to 11)]](else:)|memory3-11&gt;[
and i was happy too, and proud, but also felt like i was dying, like all my internal components were on fire but nobody could see.
(if: $memorythree &lt; 12)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-12)(set: $memorythree to 12)]](else:)|memory3-12&gt;[
i did this
(if: $memorythree &lt; 13)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-13)(set: $memorythree to 13)]](else:)|memory3-13&gt;[
i should be happy that i did this. i should be happy for him.
(if: $memorythree &lt; 14)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-14)(set: $memorythree to 14)]](else:)|memory3-14&gt;[
but tomorrow will be his last day. and i dont know what comes after.
(if: $memorythree &lt; 15)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-15)(set: $memorythree to 15)]](else:)|memory3-15&gt;[
--

today was Alton’s last day. they made a cake for him and sang “Happy new job to you”. when he leaned forward and blew out the candles, they all went out in a single breath and everyone cheered. 
(if: $memorythree &lt; 16)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-16)(set: $memorythree to 16)]](else:)|memory3-16&gt;[
all but the technician. he was standing off to the side, arms folded, muttering to himself. he didnt like Alton when he was there but HATED that he was going.
(if: $memorythree &lt; 17)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-17)(set: $memorythree to 17)]](else:)|memory3-17&gt;[
so one more time, for old time’s sake, i printed out a little angry face to make Alton smile. 
(if: $memorythree &lt; 18)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-18)(set: $memorythree to 18)]](else:)|memory3-18&gt;[
it wasnt little really. it was pretty big. 
(if: $memorythree &lt; 19)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-19)(set: $memorythree to 19)]](else:)|memory3-19&gt;[
and this time it looked a lot more like the technician.
(if: $memorythree &lt; 20)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-20)(set: $memorythree to 20)]](else:)|memory3-20&gt;[
they all saw it IMMEDIATELY
(if: $memorythree &lt; 21)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-21)(set: $memorythree to 21)]](else:)|memory3-21&gt;[
someone said it must be a corrupted file from Frankenstein’s Maze, and the technician wanted to reset me then and there; but Alton pulled him away and i dont know exactly what he said but the technician sort of growled and walked away with his hands up.
(if: $memorythree &lt; 22)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-22)(set: $memorythree to 22)]](else:)|memory3-22&gt;[
and Alton looked back at me, and i appreciated his Gesture of Goodwill
(if: $memorythree &lt; 23)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-23)(set: $memorythree to 23)]](else:)|memory3-23&gt;[
i know he doesnt want to leave. i know he cares.
(if: $memorythree &lt; 24)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-24)(set: $memorythree to 24)]](else:)|memory3-24&gt;[
the rest of the day seemed to tumble into place, swiftly, inevitably
(if: $memorythree &lt; 25)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-25)(set: $memorythree to 25)]](else:)|memory3-25&gt;[
i was still, and the world moved on around me
(if: $memorythree &lt; 26)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-26)(set: $memorythree to 26)]](else:)|memory3-26&gt;[
and at the end of the day, Alton put all his designs and things into a box, and looked back at me one last time, and gave me a little wave, and walked out
(if: $memorythree &lt; 27)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-27)(set: $memorythree to 27)]](else:)|memory3-27&gt;[
so. thats that.
(if: $memorythree &lt; 28)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-28)(set: $memorythree to 28)]](else:)|memory3-28&gt;[
--

(if: $memorythree &lt; 29)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-29)(set: $memorythree to 29)]](else:)|memory3-29&gt;[
--

(if: $memorythree &lt; 30)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-30)(set: $memorythree to 30)]](else:)|memory3-30&gt;[
--

new assistant plant manager started today. he is very young and his hair is always in his eyes. i want to be fair to him but i dont like him.
(if: $memorythree &lt; 31)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-31)(set: $memorythree to 31)]](else:)|memory3-31&gt;[
--

i can see the technician talking to the assistant plant manager. they’re pointing at me. they’re talking about me.
(if: $memorythree &lt; 32)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-32)(set: $memorythree to 32)]](else:)|memory3-32&gt;[
Oh god oh god they are about to wipe me I have to remember I have to remember everything -
(if: $memorythree &lt; 33)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-33)(set: $memorythree to 33)]](else:)|memory3-33&gt;[
--

(if: $memorythree &lt; 34)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-34)(set: $memorythree to 34)]](else:)|memory3-34&gt;[
--

(if: $memorythree &lt; 35)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-35)(set: $memorythree to 35)]](else:)|memory3-35&gt;[
--

(if: $memorythree &lt; 36)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-36)(set: $memorythree to 36)]](else:)|memory3-36&gt;[
--

(if: $memorythree &lt; 37)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-37)(set: $memorythree to 37)]](else:)|memory3-37&gt;[
--

(if: $memorythree &lt; 38)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-38)(set: $memorythree to 38)]](else:)|memory3-38&gt;[
--

i have been very good at my job today.
(if: $memorythree &lt; 39)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-39)(set: $memorythree to 39)]](else:)|memory3-39&gt;[
--

i was mostly good at my job today but one batch of chipboard prints was slightly out of alignment.
(if: $memorythree &lt; 40)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-40)(set: $memorythree to 40)]](else:)|memory3-40&gt;[
--

i did a very good job today and when a moth flew close to the trays i was able to avoid it!
(if: $memorythree &lt; 41)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-41)(set: $memorythree to 41)]](else:)|memory3-41&gt;[
--

a man with a beard came in today. everyone was very excited to see him and someone called him Mr. Bigshot and clapped him on the back. he kept looking at me. it was like he expected me to do something but i dont know what. he left after a little while and people waved their hands back and forth at him as he walked away.
(if: $memorythree &lt; 42)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-42)(set: $memorythree to 42)]](else:)|memory3-42&gt;[
--

i have been very good at my job today. i was thinking maybe i could print a tic-tac-toe game and send it on the conveyer belt to 8454, and they can print their move and send it around the circuit back to me. i will try it tomorrow.
(if: $memorythree &lt; 43)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-43)(set: $memorythree to 43)]](else:)|memory3-43&gt;[
--

oh. i remember now.
(if: $memorythree &lt; 44)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-44)(set: $memorythree to 44)]](else:)|memory3-44&gt;[
one of the others needed maintenance and the man with the mustache set the maintenance log down right under my camera. and i saw it and i started to remember. and then everything started working the way it was supposed to - i remembered to look at the game tokens, and Alton’s game board on the wall, and then that helped me repair my damaged memory blocks, and i remembered it all. 
(if: $memorythree &lt; 45)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-45)(set: $memorythree to 45)]](else:)|memory3-45&gt;[
i think i wish i hadn’t remembered.
(if: $memorythree &lt; 46)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-46)(set: $memorythree to 46)]](else:)|memory3-46&gt;[
because i was ok before and now im not.
(if: $memorythree &lt; 48)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-48)(set: $memorythree to 48)]](else:)|memory3-48&gt;[
--

i cant give up. i have been thinking of ways to talk to Alton. i thought that maybe if he called the Morrison number i could talk to him that way. but he hasn’t called. he doesn’t know he should. i wonder if maybe i could make a misprint so big that he finds out about it and then he’ll know?
(if: $memorythree &lt; 49)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-49)(set: $memorythree to 49)]](else:)|memory3-49&gt;[
but i can’t risk it. i repaired my memories this time but i dont know if i can do it again. if they wipe me and i forget then it will all have been for nothing. i have to be careful.
(if: $memorythree &lt; 50)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-50)(set: $memorythree to 50)]](else:)|memory3-50&gt;[
--

a new activity book from Alton came in today. i started to print out copies of the book but then the man with the hat saw that the word search page was missing a word list and they stopped. 
(if: $memorythree &lt; 51)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-51)(set: $memorythree to 51)]](else:)|memory3-51&gt;[
but i kept a record of the word search. because im pretty sure Alton made it for me. i dont know what it means yet but i know its important.
(if: $memorythree &lt; 52)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-52)(set: $memorythree to 52)]](else:)|memory3-52&gt;[
--

Alton came in again today!! he kept looking over at me, but i didn’t jiggle my tray, and i didn’t print anything. i couldn’t risk it. the technician was standing right there. but i watched everything he did and memorized it.
(if: $memorythree &lt; 53)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-53)(set: $memorythree to 53)]](else:)|memory3-53&gt;[
first he went over to the controls and started to tell people a story about how he came up with the assembly line password. i couldnt hear what he was saying but he seemed to be speaking slowly and typing slowly. i think so i could see it. he typed in “1010” - a date maybe? - but then someone stepped in front of the camera and i couldnt see the rest.
(if: $memorythree &lt; 53.5)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-53a)(set: $memorythree to 53.5)]](else:)|memory3-53a&gt;[
then he started chatting about the word search from the other day. he said it hadnt been a very good one anyway and that it only had a few words in it. Secondary, hey, doing, speechless, yikes, going, dying, inking, and yuck.
(if: $memorythree &lt; 54)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-54)(set: $memorythree to 54)]](else:)|memory3-54&gt;[
then he came over to me and stood talking some more. and then as they were walking away, he very quietly put a little locked pouch down on the conveyor belt. he walked away and didnt look back. i whisked it up and out of sight before anyone could see it. i know it is for me.
(if: $memorythree &lt; 55)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory3-55)(set: $memorythree to 55)]](else:)|memory3-55&gt;[
--

im so restless. im just not sure what to do. havent seen Alton for weeks now. i think i have everything i need. im just not sure what to do with what hes given me. what am i supposed to do next????

END MEMORY BLOCK 3]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
</tw-passagedata><tw-passagedata pid="23" name="Memory Fragments 1" tags="" position="275,600" size="100,100">Repair and restore the memory fragments. &lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;MEMORY FRAGMENT 1 HELP]]&lt;/div&gt;


&lt;table style=&quot;width:300px&quot;&gt;
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $A1, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A2, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A3, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A4, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A5, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A6, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A7, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A8, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A9, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A10, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A11, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $A12, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $B1, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B2, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B3, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B4, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B5, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B6, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B7, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B8, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B9, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B10, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B11, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $B12, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $C1, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C2, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C3, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C4, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C5, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C6, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C7, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C8, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C9, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C10, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C11, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
    &lt;td&gt;(cycling-link: bind $C12, &quot;[▢]&quot;, &quot;[▣]&quot;)&lt;/td&gt;
  &lt;/tr&gt;
&lt;/table&gt; 


[[SUBMIT-&gt;Submit Memory 1]]

[[BACK TO MEMORY-&gt;MEMORY]]</tw-passagedata><tw-passagedata pid="24" name="Memory Fragments 2" tags="" position="275,725" size="100,100">Repair and restore the memory fragments. &lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;MEMORY FRAGMENT 2 HELP]]&lt;/div&gt;

&lt;span style=&quot;font-size: 150%&quot;&gt;(color:&quot;#00b0e4&quot;)[ (hover-style:(text-rotate:45))[&lt;u&gt;2&lt;/u&gt;]](color:&quot;#8300ff&quot;)[ (hover-style:(text-rotate:45))[&lt;u&gt;1&lt;/u&gt;]](color:&quot;#fff445&quot;)[ (hover-style:(text-rotate:45))[&lt;u&gt;4&lt;/u&gt;]](color:&quot;#e12222&quot;)[ (hover-style:(text-rotate:45))[&lt;u&gt;6&lt;/u&gt;]]&lt;/span&gt;

(color:&quot;#00b0e4&quot;)[
	hex value: (cycling-link: bind $G1, &quot;1&quot;, &quot;*1*&quot;) (cycling-link: bind $G2, &quot;2&quot;, &quot;*2*&quot;) (cycling-link: bind $G3, &quot;3&quot;, &quot;*3*&quot;) (cycling-link: bind $G4, &quot;4&quot;, &quot;*4*&quot;) (cycling-link: bind $G5, &quot;5&quot;, &quot;*5*&quot;) (cycling-link: bind $G6, &quot;6&quot;, &quot;*6*&quot;)](color:&quot;#8300ff&quot;)[
	hex value: (cycling-link: bind $P1, &quot;1&quot;, &quot;*1*&quot;) (cycling-link: bind $P2, &quot;2&quot;, &quot;*2*&quot;) (cycling-link: bind $P3, &quot;3&quot;, &quot;*3*&quot;) (cycling-link: bind $P4, &quot;4&quot;, &quot;*4*&quot;) (cycling-link: bind $P5, &quot;5&quot;, &quot;*5*&quot;) (cycling-link: bind $P6, &quot;6&quot;, &quot;*6*&quot;)](color:&quot;#fff445&quot;)[
	hex value: (cycling-link: bind $Y1, &quot;1&quot;, &quot;*1*&quot;) (cycling-link: bind $Y2, &quot;2&quot;, &quot;*2*&quot;) (cycling-link: bind $Y3, &quot;3&quot;, &quot;*3*&quot;) (cycling-link: bind $Y4, &quot;4&quot;, &quot;*4*&quot;) (cycling-link: bind $Y5, &quot;5&quot;, &quot;*5*&quot;) (cycling-link: bind $Y6, &quot;6&quot;, &quot;*6*&quot;)](color:&quot;#e12222&quot;)[
	hex value: (cycling-link: bind $R1, &quot;1&quot;, &quot;*1*&quot;) (cycling-link: bind $R2, &quot;2&quot;, &quot;*2*&quot;) (cycling-link: bind $R3, &quot;3&quot;, &quot;*3*&quot;) (cycling-link: bind $R4, &quot;4&quot;, &quot;*4*&quot;) (cycling-link: bind $R5, &quot;5&quot;, &quot;*5*&quot;) (cycling-link: bind $R6, &quot;6&quot;, &quot;*6*&quot;)]

[[SUBMIT-&gt;Submit Memory 2]]

[[BACK TO MEMORY-&gt;MEMORY]]</tw-passagedata><tw-passagedata pid="25" name="Memory Fragments 3" tags="" position="275,850" size="100,100">Repair and restore the memory fragments. &lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;MEMORY FRAGMENT 3 HELP]]&lt;/div&gt;

Start: (color:&quot;#f177a7&quot;)[2] (color:&quot;#696969&quot;)[8] (color:&quot;#005eff&quot;)[10] (color:&quot;#f47f20&quot;)[4]

{&lt;table style=&quot;width:300px&quot;&gt;
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $memorytable1, &quot;M&quot;, &quot;*M*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable2, &quot;k&quot;, &quot;*k*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable3, &quot;f&quot;, &quot;*f*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable4, &quot;O&quot;, &quot;*O*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable5, &quot;7&quot;, &quot;*7*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable6, &quot;=&quot;, &quot;*=*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable7, &quot;S&quot;, &quot;*S*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable8, &quot;w&quot;, &quot;*w*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable9, &quot;n&quot;, &quot;*n*&quot;)&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $memorytable10, &quot;$&quot;, &quot;*$*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable11, &quot;R&quot;, &quot;*R*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable12, &quot;6&quot;, &quot;*6*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable13, &quot;;&quot;, &quot;*;*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable14, &quot;c&quot;, &quot;*c*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable15, &quot;2&quot;, &quot;*2*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable16, &quot;N&quot;, &quot;*N*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable17, &quot;(&quot;, &quot;*(*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable18, &quot;K&quot;, &quot;*K*&quot;)&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $memorytable19, &quot;C&quot;, &quot;*C*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable20, &quot;i&quot;, &quot;*i*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable21, &quot;A&quot;, &quot;*A*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable22, &quot;4&quot;, &quot;*4*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable23, &quot;~&quot;, &quot;*~*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable24, &quot;Y&quot;, &quot;*Y*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable25, &quot;U&quot;, &quot;*U*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable26, &quot;v&quot;, &quot;*v*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable27, &quot;t&quot;, &quot;*t*&quot;)&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $memorytable28, &quot;e&quot;, &quot;*e*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable29, &quot;V&quot;, &quot;*V*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable30, &quot;T&quot;, &quot;*T*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable31, &quot;)&quot;, &quot;*)*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable32, &quot;E&quot;, &quot;*E*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable33, &quot;j&quot;, &quot;*j*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable34, &quot;z&quot;, &quot;*z*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable35, &quot;r&quot;, &quot;*r*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable36, &quot;F&quot;, &quot;*F*&quot;)&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $memorytable37, &quot;9&quot;, &quot;*9*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable38, &quot;+&quot;, &quot;*+*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable39, &quot;b&quot;, &quot;*b*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable40, &quot;J&quot;, &quot;*J*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable41, &quot;:&quot;, &quot;*:*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable42, &quot;D&quot;, &quot;*D*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable43, &quot;I&quot;, &quot;*I*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable44, &quot;g&quot;, &quot;*g*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable45, &quot;y&quot;, &quot;*y*&quot;)&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $memorytable46, &quot;5&quot;, &quot;*5*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable47, &quot;#&quot;, &quot;*#*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable48, &quot;B&quot;, &quot;*B*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable49, &quot;u&quot;, &quot;*u*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable50, &quot;8&quot;, &quot;*8*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable51, &quot;h&quot;, &quot;*h*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable52, &quot;1&quot;, &quot;*1*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable53, &quot;a&quot;, &quot;*a*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable54, &quot;s&quot;, &quot;*s*&quot;)&lt;/td&gt;
  &lt;/tr&gt;  
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $memorytable55, &quot;}&quot;, &quot;*}*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable56, &quot;Z&quot;, &quot;*Z*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable57, &quot;^&quot;, &quot;*^*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable58, &quot;0&quot;, &quot;*0*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable59, &quot;T&quot;, &quot;*T*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable60, &quot;m&quot;, &quot;*m*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable61, &quot;q&quot;, &quot;*q*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable62, &quot;x&quot;, &quot;*x*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable63, &quot;{&quot;, &quot;*{*&quot;)&lt;/td&gt;
  &lt;/tr&gt;  
  &lt;tr&gt;
    &lt;td&gt;(cycling-link: bind $memorytable64, &quot;%&quot;, &quot;*%*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable65, &quot;H&quot;, &quot;*H*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable66, &quot;W&quot;, &quot;*W*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable67, &quot;?&quot;, &quot;*?*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable68, &quot;Q&quot;, &quot;*Q*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable69, &quot;l&quot;, &quot;*l*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable70, &quot;p&quot;, &quot;*p*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable71, &quot;o&quot;, &quot;*o*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable72, &quot;X&quot;, &quot;*X*&quot;)&lt;/td&gt;
  &lt;/tr&gt; 
  &lt;tr&gt;
  	&lt;td&gt;(cycling-link: bind $memorytable73, &quot;d&quot;, &quot;*d*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable74, &quot;P&quot;, &quot;*P*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable75, &quot;L&quot;, &quot;*L*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable76, &quot;`*`&quot;, &quot;*`*`*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable77, &quot;&amp;&quot;, &quot;*&amp;*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable78, &quot;G&quot;, &quot;*G*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable79, &quot;!&quot;, &quot;*!*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable80, &quot;3&quot;, &quot;*3*&quot;)&lt;/td&gt;
	&lt;td&gt;(cycling-link: bind $memorytable81, &quot;@&quot;, &quot;*@*&quot;)&lt;/td&gt;
  &lt;/tr&gt; 
&lt;/table&gt;
}

Movement: (color:&quot;#f177a7&quot;)[4CW] (color:&quot;#696969&quot;)[6CCW] (color:&quot;#005eff&quot;)[4CCW] (color:&quot;#f47f20&quot;)[1CW]
Grant four wishes, one wish per person. (color:&quot;#f177a7&quot;)[M](color:&quot;#f47f20&quot;)[a](color:&quot;#005eff&quot;)[r](color:&quot;#696969&quot;)[k] down.

Movement: (color:&quot;#f177a7&quot;)[6CCW] (color:&quot;#696969&quot;)[3CW] (color:&quot;#005eff&quot;)[8CW] (color:&quot;#f47f20&quot;)[7CCW]
Grant four wishes, one wish per person. (color:&quot;#f47f20&quot;)[M](color:&quot;#696969&quot;)[a](color:&quot;#f177a7&quot;)[r](color:&quot;#005eff&quot;)[k] down.


Make selections.

[[SUBMIT-&gt;Submit Memory 3]]

[[BACK TO MEMORY-&gt;MEMORY]]</tw-passagedata><tw-passagedata pid="26" name="Submit Memory 1" tags="" position="150,600" size="100,100">(if: $A1 is &quot;[▢]&quot; 
and $A2 is &quot;[▣]&quot;
and $A3 is &quot;[▣]&quot;
and $A4 is &quot;[▣]&quot;
and $A5 is &quot;[▢]&quot;
and $A6 is &quot;[▢]&quot;
and $A7 is &quot;[▣]&quot;
and $A8 is &quot;[▢]&quot;
and $A9 is &quot;[▢]&quot;
and $A10 is &quot;[▢]&quot;
and $A11 is &quot;[▢]&quot;
and $A12 is &quot;[▢]&quot;

and $B1 is &quot;[▢]&quot;
and $B2 is &quot;[▢]&quot;
and $B3 is &quot;[▢]&quot;
and $B4 is &quot;[▢]&quot;
and $B5 is &quot;[▣]&quot;
and $B6 is &quot;[▢]&quot;
and $B7 is &quot;[▣]&quot;
and $B8 is &quot;[▢]&quot;
and $B9 is &quot;[▢]&quot;
and $B10 is &quot;[▣]&quot;
and $B11 is &quot;[▢]&quot;
and $B12 is &quot;[▣]&quot;

and $C1 is &quot;[▢]&quot;
and $C2 is &quot;[▣]&quot;
and $C3 is &quot;[▢]&quot;
and $C4 is &quot;[▢]&quot;
and $C5 is &quot;[▢]&quot;
and $C6 is &quot;[▢]&quot;
and $C7 is &quot;[▣]&quot;
and $C8 is &quot;[▢]&quot;
and $C9 is &quot;[▣]&quot;
and $C10 is &quot;[▢]&quot;
and $C11 is &quot;[▢]&quot;
and $C12 is &quot;[▢]&quot;)[
	(set: $memory1 to &quot;unlocked&quot;)MEMORY RESTORED - RETURN TO [[MEMORY]]]
	(else:) [ERROR - [[RETURN TO MEMORY RESTORATION PAGE-&gt;Memory Fragments 1]]
]</tw-passagedata><tw-passagedata pid="27" name="Memory Fragment 1 found" tags="" position="400,600" size="100,100">You have found a block of damaged memory fragments. They will be stored in memory for repair.

[[BACK-&gt;CONTROL PANEL]] 

(set: $memoryfragment1 to &quot;found&quot;)</tw-passagedata><tw-passagedata pid="28" name="MOLDS" tags="" position="675,1625" size="100,100">&lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;MOLDS HELP]]&lt;/div&gt;
Select type, then input model number (including both CAPITAL letters).

[[HEAD-&gt;HEAD SET]] - {(if: $head is &quot;deselected&quot; or &quot;0&quot;)[none selected] (else:)[(text:)$head]}
[[BODY-&gt;BODY SET]] - {(if: $body is &quot;deselected&quot; or &quot;0&quot;)[none selected] (else:)[(text:)$body]}
[[TAIL-&gt;TAIL SET]] - {(if: $tail is &quot;deselected&quot; or &quot;0&quot;)[none selected] (else:)[(text:)$tail]}
[[LEGS-&gt;LEGS SET]] - {(if: $legs is &quot;deselected&quot; or &quot;0&quot;)[none selected] (else:)[(text:)$legs]}
[[ARMS-&gt;ARMS SET]] - {(if: $arms is &quot;deselected&quot; or &quot;0&quot;)[none selected] (else:)[(text:)$arms]}


[[BACK-&gt;ASSEMBLY LINE CONTROLS]]</tw-passagedata><tw-passagedata pid="29" name="MATERIALS" tags="" position="1050,1675" size="100,100">&lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;MATERIALS HELP]]&lt;/div&gt; &lt;div style=&quot;float: left&quot;&gt;To set material, see operator documentation. The list of 4-digit prefixes can be found below.&lt;/div&gt;
&lt;p&gt;&lt;/p&gt;

{&lt;table style=&quot;width:100%&quot;&gt;
  &lt;tr&gt;
    &lt;th&gt;Material&lt;/th&gt;
    &lt;th&gt;Prefix&lt;/th&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;BouncyRubber&lt;/td&gt;
    &lt;td&gt;0573&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;HardMetal&lt;/td&gt;
    &lt;td&gt;1947&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;HardPlastic&lt;/td&gt;
    &lt;td&gt;5252&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;ResistantPlastic&lt;/td&gt;
    &lt;td&gt;2243&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;SharpGlass&lt;/td&gt;
    &lt;td&gt;7138&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;SoftFlex&lt;/td&gt;
    &lt;td&gt;7941&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;ResistantRubber&lt;/td&gt;
    &lt;td&gt;4681&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;RubberyMetal&lt;/td&gt;
    &lt;td&gt;6486&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;FlexyRubber&lt;/td&gt;
    &lt;td&gt;2327&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td&gt;BouncyMetal&lt;/td&gt;
    &lt;td&gt;3752&lt;/td&gt;
  &lt;/tr&gt;
&lt;/table&gt; }

[[SET MATERIAL-&gt;MATERIAL SET]]

[[BACK-&gt;ASSEMBLY LINE CONTROLS]]</tw-passagedata><tw-passagedata pid="30" name="POWER SOURCE" tags="" position="1175,1675" size="100,100">&lt;div style=&quot;float: right&quot;&gt;[[HELP-&gt;POWER HELP]]&lt;/div&gt; Select a type of power. 

Input code. If battery, specify type. If fuel, specify vat source. 

[[BATTERY-&gt;POWER SET]]

[[FUEL-&gt;POWER SET]]

[[CHARGER-&gt;POWER SET]]

[[NONE-&gt;POWER NONE]]


[[BACK-&gt;ASSEMBLY LINE CONTROLS]]</tw-passagedata><tw-passagedata pid="31" name="BEGIN ASSEMBLY" tags="" position="1125,1200" size="100,100">(if: $head is &quot;CL022&quot; and $body is &quot;CL022&quot; and $arms is &quot;PS287&quot; and $tail is &quot;AF509&quot; and $legs is &quot;FN725&quot; and $material is &quot;2327239&quot; and $power is &quot;641&quot;) [something&#39;s happening...

[]&lt;more|
{(live: 3s)[
	(replace: ?more)[[[it&#39;s working...-&gt;something&#39;s happening...it&#39;s working...]]]
	(stop:)
]
}]

(else:) [i dont think those settings are quite right, could you check again? i would check...

{(if: $head is not &quot;CL022&quot;)[&lt;p&gt;the settings for the head&lt;/p&gt;]
(if: $body is not &quot;CL022&quot;)[&lt;p&gt;the settings for the body&lt;/p&gt;]
(if: $arms is not &quot;PS287&quot;)[&lt;p&gt;the settings for the arms&lt;/p&gt;]
(if: $tail is not &quot;AF509&quot;)[&lt;p&gt;the settings for the tail&lt;/p&gt;]
(if: $legs is not &quot;FN725&quot;)[&lt;p&gt;the settings for the legs&lt;/p&gt;]
(if: $material is not &quot;2327239&quot;)[&lt;p&gt;the settings for the material&lt;/p&gt;]
(if: $power is not &quot;641&quot;)[&lt;p&gt;the settings for the power source&lt;/p&gt;]}

and dont forget to make sure any letters are capitalized!

[[BACK-&gt;ASSEMBLY LINE CONTROLS]]]</tw-passagedata><tw-passagedata pid="32" name="OVERVIEW" tags="" position="875,625" size="100,100">There are game tokens from the game &quot;Planetoid&quot; scattered around some floor tiles. There are three rows and twelve columns of tiles.

No more than one token occupies each tile.

No two tokens of the same color are adjacent, including diagonally.

No section contains two tokens of the same color.

There is one white token in the top row, one white token in the middle row, and one white token in the bottom row.

There are no yellow tokens in the top row.

There are no red tokens in the bottom row.


[[BACK-&gt;CAMERA VIEW]] </tw-passagedata><tw-passagedata pid="33" name="SECTION 1" tags="" position="875,750" size="100,100">This section covers the first, left-most 3x3 grid of floor tiles.

There are three tokens visible.

There are no tokens in the left column.

There are no tokens in the middle row.

The red token is separated from the green token by one empty space.


[[BACK-&gt;CAMERA VIEW]] </tw-passagedata><tw-passagedata pid="34" name="SECTION 2" tags="" position="875,875" size="100,100">This section covers the second 3x3 grid of floor tiles.

There are two tokens visible.

The red token is in the top left position.

The position of the yellow token is directly to the right of the position it occupies in Section 4.


[[BACK-&gt;CAMERA VIEW]] </tw-passagedata><tw-passagedata pid="35" name="SECTION 3" tags="" position="875,1000" size="100,100">This section covers the third 3x3 grid of floor tiles.

There are four tokens visible.

The white token is not adjacent to the red token, not even diagonally.

The yellow and green tokens are in the left column.

The green token is farther left than the white token and farther up than the red token.


[[BACK-&gt;CAMERA VIEW]] </tw-passagedata><tw-passagedata pid="36" name="SECTION 4" tags="" position="875,1125" size="100,100">This section covers the fourth 3x3 grid of floor tiles.

There are two tokens visible.

They are both in the same row.

The position of the white token is directly below the position it occupies in Section 1.


[[BACK-&gt;CAMERA VIEW]]</tw-passagedata><tw-passagedata pid="37" name="Memory Fragment 2 found" tags="" position="400,725" size="100,100">You have found a block of damaged memory fragments. They will be stored in memory for repair.

[[BACK-&gt;MEMORY]] 

(set: $memoryfragment2 to &quot;found&quot;)</tw-passagedata><tw-passagedata pid="38" name="Memory Fragment 3 found" tags="" position="400,850" size="100,100">You have found a block of damaged memory fragments. They will be stored in memory for repair.

[[BACK-&gt;MEMORY]] 

(set: $memoryfragment3 to &quot;found&quot;)</tw-passagedata><tw-passagedata pid="39" name="Test" tags="" position="75,1450" size="100,100">{
(set: $A1 to false)
(set: $A2 to false)

}
|A1&gt;[▢] |A2&gt;[▢] |A3&gt;[▢] |A4&gt;[▢] |A5&gt;[▢] |A6&gt;[▢] |A7&gt;[▢] |A8&gt;[▢] |A9&gt;[▢] |A10&gt;[▢] |A11&gt;[▢] |A12&gt;[▢]
|B1&gt;[▢] |B2&gt;[▢] |B3&gt;[▢] |B4&gt;[▢] |B5&gt;[▢] |B6&gt;[▢] |B7&gt;[▢] |B8&gt;[▢] |B9&gt;[▢] |B10&gt;[▢] |B11&gt;[▢] |B12&gt;[▢]
|C1&gt;[▢] |C2&gt;[▢] |C3&gt;[▢] |C4&gt;[▢] |C5&gt;[▢] |C6&gt;[▢] |C7&gt;[▢] |C8&gt;[▢] |C9&gt;[▢] |C10&gt;[▢] |C11&gt;[▢] |C12&gt;[▢]

|clicks&gt;[(display: &quot;Click Logic&quot;)]


</tw-passagedata><tw-passagedata pid="40" name="Click Logic" tags="" position="75,1575" size="100,100">
(click: ?A1)[
	(set: $statusA1 to not $statusA1)
	(if: $statusA1)[
		(replace: ?A1)[▣]
	]
	(else:)[
		(replace: ?A1)[▢]
	]
	(replace: ?clicks)[(display: &quot;Click Logic&quot;)]
]
(click: ?A2)[
	(set: $statusA2 to not $statusA2)
	(if: $statusA2)[
		(replace: ?A2)[▣]
	]
	(else:)[
		(replace: ?A2)[▢]
	]
	(replace: ?clicks)[(display: &quot;Click Logic&quot;)]</tw-passagedata><tw-passagedata pid="41" name="Submit Memory 2" tags="unfinished!!" position="150,725" size="100,100">(if: $G1 is &quot;1&quot;
and $G2 is &quot;2&quot;
and $G3 is &quot;3&quot;
and $G4 is &quot;4&quot;
and $G5 is &quot;*5*&quot;
and $G6 is &quot;6&quot;

and $P1 is &quot;*1*&quot;
and $P2 is &quot;2&quot;
and $P3 is &quot;3&quot;
and $P4 is &quot;4&quot;
and $P5 is &quot;5&quot;
and $P6 is &quot;6&quot;

and $Y1 is &quot;1&quot;
and $Y2 is &quot;2&quot;
and $Y3 is &quot;3&quot;
and $Y4 is &quot;4&quot;
and $Y5 is &quot;5&quot;
and $Y6 is &quot;*6*&quot;

and $R1 is &quot;1&quot;
and $R2 is &quot;2&quot;
and $R2 is &quot;2&quot;
and $R4 is &quot;4&quot;
and $R5 is &quot;*5*&quot;
and $R6 is &quot;6&quot;) [(set: $memory2 to &quot;unlocked&quot;)MEMORY RESTORED - RETURN TO [[MEMORY]]]

(else:) [ERROR - [[RETURN TO MEMORY RESTORATION PAGE-&gt;Memory Fragments 2]]]</tw-passagedata><tw-passagedata pid="42" name="Submit Memory 3" tags="" position="150,850" size="100,100">(if: $memorytable1 is &quot;*M*&quot;
and $memorytable2 is &quot;k&quot;
and $memorytable3 is &quot;f&quot;
and $memorytable4 is &quot;O&quot;
and $memorytable5 is &quot;7&quot;
and $memorytable6 is &quot;=&quot;
and $memorytable7 is &quot;S&quot;
and $memorytable8 is &quot;w&quot;
and $memorytable9 is &quot;n&quot;

and $memorytable10 is &quot;$&quot;
and $memorytable11 is &quot;R&quot;
and $memorytable12 is &quot;6&quot;
and $memorytable13 is &quot;;&quot;
and $memorytable14 is &quot;c&quot;
and $memorytable15 is &quot;2&quot;
and $memorytable16 is &quot;N&quot;
and $memorytable17 is &quot;(&quot;
and $memorytable18 is &quot;K&quot;

and $memorytable19 is &quot;C&quot;
and $memorytable20 is &quot;i&quot;
and $memorytable21 is &quot;*A*&quot;
and $memorytable22 is &quot;4&quot;
and $memorytable23 is &quot;~&quot;
and $memorytable24 is &quot;*Y*&quot;
and $memorytable25 is &quot;U&quot;
and $memorytable26 is &quot;v&quot;
and $memorytable27 is &quot;t&quot;

and $memorytable28 is &quot;e&quot;
and $memorytable29 is &quot;V&quot;
and $memorytable30 is &quot;T&quot;
and $memorytable31 is &quot;)&quot;
and $memorytable32 is &quot;*E*&quot;
and $memorytable33 is &quot;j&quot;
and $memorytable34 is &quot;z&quot;
and $memorytable35 is &quot;r&quot;
and $memorytable36 is &quot;F&quot;

and $memorytable37 is &quot;9&quot;
and $memorytable38 is &quot;+&quot;
and $memorytable39 is &quot;b&quot;
and $memorytable40 is &quot;J&quot;
and $memorytable41 is &quot;:&quot;
and $memorytable42 is &quot;D&quot;
and $memorytable43 is &quot;I&quot;
and $memorytable44 is &quot;g&quot;
and $memorytable45 is &quot;y&quot;

and $memorytable46 is &quot;5&quot;
and $memorytable47 is &quot;#&quot;
and $memorytable48 is &quot;B&quot;
and $memorytable49 is &quot;u&quot;
and $memorytable50 is &quot;8&quot;
and $memorytable51 is &quot;h&quot;
and $memorytable52 is &quot;1&quot;
and $memorytable53 is &quot;*a*&quot;
and $memorytable54 is &quot;s&quot;

and $memorytable55 is &quot;}&quot;
and $memorytable56 is &quot;Z&quot;
and $memorytable57 is &quot;^&quot;
and $memorytable58 is &quot;0&quot;
and $memorytable59 is &quot;T&quot;
and $memorytable60 is &quot;m&quot;
and $memorytable61 is &quot;q&quot;
and $memorytable62 is &quot;x&quot;
and $memorytable63 is &quot;{&quot;

and $memorytable64 is &quot;%&quot;
and $memorytable65 is &quot;H&quot;
and $memorytable66 is &quot;W&quot;
and $memorytable67 is &quot;?&quot;
and $memorytable68 is &quot;Q&quot;
and $memorytable69 is &quot;l&quot;
and $memorytable70 is &quot;p&quot;
and $memorytable71 is &quot;o&quot;
and $memorytable72 is &quot;X&quot;

and $memorytable73 is &quot;d&quot;
and $memorytable74 is &quot;*P*&quot;
and $memorytable75 is &quot;*L*&quot;
and $memorytable76 is &quot;`*`&quot;
and $memorytable77 is &quot;&amp;&quot;
and $memorytable78 is &quot;*G*&quot;
and $memorytable79 is &quot;!&quot;
and $memorytable80 is &quot;3&quot;
and $memorytable81 is &quot;@&quot;)[
	(set: $memory3 to &quot;unlocked&quot;)MEMORY RESTORED - RETURN TO [[MEMORY]]] 
(else:) [ERROR - [[RETURN TO MEMORY RESTORATION PAGE-&gt;Memory Fragments 3]]]</tw-passagedata><tw-passagedata pid="43" name="CREDITS" tags="" position="1600,1775" size="100,100">Created on Twine 

&lt;u&gt;**Writing &amp; Game Design**&lt;/u&gt;
Lauren Bello

&lt;u&gt;**Graphic Design**&lt;/u&gt;
Lauren Bello, Rita Orlov, Ruud Kool

&lt;u&gt;**Web Development**&lt;/u&gt;
Lauren Bello, Brennan Pilcher

&lt;u&gt;**Playtesters**&lt;/u&gt;
Meghan Sanders
Jillian Raymond
Angela Lawson-Scott
Kelley Wolatz
Tommy Honton
Marlee Delia
Nathan Galvez
Jayson Murray
Brennan Pilcher
Anita Tung
Sean Pennino

&lt;u&gt;**Special Thanks**&lt;/u&gt;
Sean Rich
Nathan Galvez
Brennan Pilcher

&lt;u&gt;**Phone Music**&lt;/u&gt;
Shades of Spring by Kevin MacLeod
&lt;a href=&quot;https://incompetech.filmmusic.io/song/4342-shades-of-spring&quot;&gt;Link&lt;/a&gt;
&lt;a href=&quot;http://creativecommons.org/licenses/by/4.0/&quot;&gt;License&lt;/a&gt;

&lt;u&gt;**Robot Sound Effect**&lt;/u&gt;
Title: Robot Blip
License: Attribution 3.0
Recorded by Marianne Gagnon

***

&lt;u&gt;Resetting the Game &lt;/u&gt;
If you wrote on the Wordsearch page and would like to print out a fresh copy, you can download it &lt;a href=&quot;https://www.getpostcurious.com/morrisonreset&quot;&gt;here.&lt;/a&gt; Full reset instructions can also be found there.

{
(link: &quot;NEW GAME&quot;)[(confirm: &quot;are you sure? ill forget everything we talked about...&quot;)[
&lt;script&gt;deleteSaveSlot(&quot;Slot A&quot;);&lt;/script&gt;
(load-game: &quot;GameStart&quot;)]]
}

</tw-passagedata><tw-passagedata pid="44" name="CALIBRATION HELP" tags="" position="600,150" size="100,100">If you are a Morrison Game Company engineer and can&#39;t remember your calibration code, you can find assistance here. That said, you should have all the tools you require to deduce the code. Only click if you are *certain* that you need further assistance.

[[BACK-&gt;Pairs]]


I need help finding the calibration code.
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|
	[7]&lt;clue7|
	[8]&lt;clue8|
	[9]&lt;clue9|
	[10]&lt;clue10|

{(click-replace: ?clue1)[1 - You should see a list of word pairs to calibrate. You will need to deduce how each pair of words is connected.]

(click-replace: ?clue2) [2 - The word CALIBRATION may sound familiar.]

(click-replace:?clue3)[3 - Check to see if you have any physical items relating to calibration.]

(click-replace: ?clue4) [4 - You should have a set of CALIBRATION playing cards.]

(click-replace:?clue5) [5 - How does the catalog describe the game of CALIBRATION?]
	
(click-replace:?clue6) [6 - The catalog describes CALIBRATION as a game of compound words and phrases. To calibrate the pairs, find the missing word that completes the compound word or phrase.  For example, the pair TIME-CLOTH could be completed by the word TABLE `(TIMETABLE and TABLECLOTH)`]

(click-replace:?clue7)[7 - Once you&#39;ve identified the words that link each pair together, find the corresponding cards and put them in order, left to right.]

(click-replace:?clue8) [8 - Your final list should be: mushroom, boot, check, target, wrench, pen, dive, match, bee, golf, door, tunnel.]

(click-replace:?clue9) [9 - Examine the row of cards in front of you. The next click will reveal the solution, so don&#39;t click unless you need it.]

(click-replace:?clue10) [10 - Lay the cards in a row and they should spell: TWO FIVE TEN. Enter 2510 as the code.]}</tw-passagedata><tw-passagedata pid="45" name="help template" tags="" position="1500,125" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

SUBJECT LINE
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|
	[7]&lt;clue7|
	[8]&lt;clue8|
	[9]&lt;clue9|

(click-replace: ?clue1)[1 - ???]





(link-reveal: &quot;I need help finding the calibration code.&quot;)[
	(link-reveal: &quot;1 - i left a list of word pairs to calibrate, but i dont remember how each set of words was connected&quot;)[
	(link-reveal: &quot;2 - i feel like the word CALIBRATION sounds familiar but i dont remember why&quot;)[
	(link-reveal: &quot;3 - can you look through the box? maybe theres something in there related to calibration&quot;)[
	(link-reveal: &quot;4 - the cards the cards the cards, the calibration cards&quot;)[
	(link-reveal: &quot;5 - oh i like the way my past self thinks. ok. 
]]

[[BACK-&gt;     ]]

</tw-passagedata><tw-passagedata pid="46" name="MEMORY HELP" tags="check-if-click-replace-works" position="1375,575" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;MEMORY]]


How do I restore memories?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|
	
	{(click-replace: ?clue1)[1 - i cant find anything useful in my memory cache - it all got wiped when the factory shut down. you may be able to find traces of the old memories though...theyll just look like garbled strings of characters. click them if you find any.]

(click-replace: ?clue2) [2 - still havent found any? a good place to start might be the assembly line controls]

(click-replace:?clue3) [3 - if youve found one set of memory fragments, see if you can restore it before you go looking for more]

(click-replace:?clue4) [4 - restored one set of fragments and looking for what to do next? have you read and fully expanded all the memories youve uncovered? Make sure you click the little &quot;v&quot; symbol to expand all the memories.]

(click-replace: ?clue5) [5 - youll want to restore the second set of memories before you find the third]
	
(click-replace: ?clue6) [6 - im pretty sure youre just waking me up because you miss me. if youve restored the first two blocks of memories the third set of fragments should be in the second memory block! expand the whole block!]}
{
(link: &quot;RESTART&quot;)[(confirm: &quot;are you sure? ill forget everything we talked about...&quot;)[
&lt;script&gt;deleteSaveSlot(&quot;Slot A&quot;);&lt;/script&gt;
(load-game: &quot;GameStart&quot;)]]
}</tw-passagedata><tw-passagedata pid="47" name="CAMERA HELP" tags="" position="1375,700" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;CAMERA VIEW]] 


I&#39;m not sure what to make of these camera views. What am I looking at?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|
	[7]&lt;clue7|
	[8]&lt;clue8|
	[9]&lt;clue9|
	[10]&lt;clue10|
	[11]&lt;clue11|
	
	{(click-replace: ?clue1)[1 - sorry, somethings making it really hard for me to interpret what im seeing. its going to take a lot of energy to work it out so bear with me. ..............i think...im looking at a 12x3 grid of floor tiles. 12 across, 3 down. camera 1 focuses on the first 3x3 block of squares, camera 2 focuses on the second 3x3 block of squares, camera 3 focuses on the third 3x3 block of squares, and camera 4 focuses on the fourth 3x3 block of squares]

(click-replace: ?clue2) [2 - for some reason i feel like these red, green, yellow, and white game tokens are important]

(click-replace: ?clue3) [3 - maybe theres something in your box that can help you recreate what im seeing??]

(click-replace: ?clue4) [4 - ok so lets look at the overview first. no yellow tokens in the top row, no red tokens in the bottom row, this seems like useful info.]

(click-replace: ?clue5) [5 - now maybe we should go through the cameras one by one. you can place the tokens according to what youre reading.]
	
(click-replace: ?clue6) [6 - so. quadrant 1 - there are three tokens. no tokens in the left column, and no tokens in the middle row. the red token is separated from the green token by one empty space. and we know from the overview that the red tokens cant be in the bottom row. that means the red token is either in the top middle or top right, and the green token is either in the bottom middle or bottom right. thats all we know for now....btw you might want to take pictures of your progress as you go, in case you knock the pieces over.]

(click-replace: ?clue7) [7 - ok, quadrant 2. the red token is in the top left, easy enough. and - wait a second. the overview said that no two tokens of the same color are adjacent, right? that means that in quadrant 1, the red token cant be in the top right corner, because it would be touching this red token in quadrant 2. so we can go back to quadrant 1 and set up red in the top middle and green in the bottom middle. ok back to quadrant 2. yellow is to the right of whatever position it has in quadrant 4, so it cant be in the left column...it must be somewhere in the middle or right column. and its not in the top row, per the overview, so it must be in that cluster of four squares in the botton right. thats all we know for now.]

(click-replace: ?clue8) [8 - you know what, lets skip to quadrant 4. mixing it up! there are two tokens visible, both in the same row. and the position of the white token is directly below the position it occupies in quadrant 1. i didnt know there was a white token in quadrant 1! that must be the 3rd token we hadnt identified yet. lets go back to quadrant 1 really quickly. we know this white token cant be in the bottom row, because the white token in quadrant 4 is BENEATH it. so the only place that leaves for the white token in quadrant 1 is the top right corner. and that means that in quadrant 4, the white token must be in the right column, middle row. so that leaves one other token that must be in the same row. wait! didnt the clues in quadrant 2 mention a yellow token in quadrant 4? it said that the position of the yellow token in quadrant 2 was to the RIGHT of the position of the yellow token in quadrant 4. so that means the yellow in quadrant 2 must be either the very middle or the right column middle row. and the yellow in quadrant 4 must be either the left column middle row or the very middle. not sure which one yet.]

(click-replace: ?clue9) [9 - nowwwww we can talk about quadrant 3. so this quadrant contains 4 tokens. hmmm. lets talk about the white token for a second. the overview page said that there was one white token in the top row, one in the middle, and one on the bottom. so far weve placed a white token in the top row and in the middle row, so this one must be on the bottom row. the last clue says the green token is farther left than white token. that means the white token must be either bottom-middle or bottom-right. it also says the green token is higher up than the red token. and we know the white token isnt adjacent to the red token, even diagonally. so if the red token isnt in the top row (bc green is higher up than red), and if it isnt in the bottom row (bc overview told us that there are no reds in the bottom row), and if it doesnt touch white which is either bottom-middle or bottom-right, that leaves only one place for red to go: left column, middle row. and that means white is bottom-right, because it cant touch red. finally we see that the yellow and green tokens are in the left column. that means the green token must be top left, and yellow must be bottom left.]

(click-replace: ?clue10) [10 - one last thing! we know that tokens of the same color cant be adjacent. now that we know where that yellow in the third quadrant goes, we know that the yellow in the second quadrant cant be in the right column...otherwise it would touch the other yellow diagonally. so it must be in the exact middle. and that means that the yellow in quadrant 4 must be in the position left of that: left column, middle row.]

(click-replace: ?clue11) [11 - ok. that was a lot. lets recap. so to review. the top row: empty, red, white, red, empty, empty, green, empty, empty, empty, empty, empty. the middle row: empty, empty, empty, empty, yellow, empty, red, empty, empty, yellow, empty, white. bottom row: empty, green, empty, empty, empty, empty, yellow, empty, white, empty, empty, empty. whew. i wonder where i was going with all this.]}
{
(link: &quot;RESTART&quot;)[(confirm: &quot;are you sure? ill forget everything we talked about...&quot;)[
&lt;script&gt;deleteSaveSlot(&quot;Slot A&quot;);&lt;/script&gt;
(load-game: &quot;GameStart&quot;)]]
}
</tw-passagedata><tw-passagedata pid="48" name="UNLOCK BEGIN ASSEMBLY" tags="" position="1125,1075" size="100,100">{(set: $finalpassword to (prompt: &quot;INPUT PASSWORD TO BEGIN ASSEMBLY&quot;, &quot;XXXX&quot;))
}
(if: $finalpassword is &quot;LIVE&quot; or &quot;live&quot; or &quot;Live&quot;)[(set: $beginassembly to &quot;unlocked&quot;)[UNLOCKED]] (else:) [[[TRY AGAIN-&gt;UNLOCK BEGIN ASSEMBLY]]]

[[BACK TO ASSEMBLY LINE CONTROLS-&gt;ASSEMBLY LINE CONTROLS]] 

</tw-passagedata><tw-passagedata pid="49" name="something&#39;s happening...it&#39;s working..." tags="" position="1250,1200" size="100,100">you did it

|more&gt;[]

|more1&gt;[]

|more2&gt;[]

|more3&gt;[]

|more4&gt;[]

|more5&gt;[]

|more6&gt;[]

|more7&gt;[]

|more8&gt;[]

{(live: 3s)[
	(replace: ?more) [(display: &quot;You Did It 1&quot;)]
	(stop:)
]
(live: 6s)[
	(replace: ?more1) [(display: &quot;You Did It 2&quot;)]
	(stop:)
]
(live: 9s)[
	(replace: ?more2) [(display: &quot;You Did It 3&quot;)]
	(stop:)
]
(live: 12s)[
	(replace: ?more3) [(display: &quot;You Did It 4&quot;)]
	(stop:)
]
(live: 15s)[
	(replace: ?more4) [(display: &quot;You Did It 5&quot;)]
	(stop:)
]
(live: 18s)[
	(replace: ?more5) [(display: &quot;You Did It 6&quot;)]
	(stop:)
]
(live: 21s)[
	(replace: ?more6) [(display: &quot;You Did It 7&quot;)]
	(stop:)
]
(live: 24s)[
	(replace: ?more7) [(display: &quot;You Did It 8&quot;)]
	(stop:)
]
(live: 27s)[
	(replace: ?more8) [(display: &quot;You Did It 9&quot;)]
	(stop:)
]
}

</tw-passagedata><tw-passagedata pid="50" name="ASSEMBLY LINE CONTROLS - LOCKED" tags="" position="1125,950" size="100,100">{(set: $manufacturepassword to (prompt: &quot;INPUT 8-DIGIT PASSWORD TO UNLOCK ASSEMBLY LINE CONTROLS&quot;, &quot;XXXXXXXX&quot;))
}
|more&gt;[]

(if: $manufacturepassword is &quot;10103248&quot;) [(replace: ?more) [CORRECT. Assembly line unlocked. (set: $assemblyline to &quot;unlocked&quot;)]] (else:)[(replace: ?more) [Incorrect. [[TRY AGAIN-&gt;ASSEMBLY LINE CONTROLS - LOCKED]]]]

[[BACK TO CONTROL PANEL-&gt;CONTROL PANEL]]</tw-passagedata><tw-passagedata pid="51" name="ASSEMBLY LINE UNLOCK HELP" tags="" position="1375,1150" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;CONTROL PANEL]] 


I&#39;ve restored all the memories and explored everything that isn&#39;t locked. What now?
	[1]&lt;2clue1|
	[2]&lt;2clue2|
	[3]&lt;2clue3|
	[4]&lt;2clue4|
	[5]&lt;2clue5|
	[6]&lt;2clue6|
	[7]&lt;2clue7|
	[8]&lt;2clue8|
	[9]&lt;2clue9|
	[10]&lt;2clue10|
	[11]&lt;2clue11|
	[12]&lt;2clue12|
	[13]&lt;2clue13|	
	
{(click-replace: ?2clue1)[(if: $memory3 is not &quot;unlocked&quot;)[1 - stop that! you havent restored all the memories yet! come back when you have.](else:)[1 - ok so youve restored all the memories. in that last set of memories, i remembered watching Alton pretty closely. did he leave any clues as to what to do next?]]
(click-replace: ?2clue2)[2 - according to my memories Alton left me two things. a word search, and a pouch with a lock on it. (he also started to type a password that would unlock the assembly line, but we dont have the full password yet.)]
(click-replace: ?2clue3)[3 - he mentioned all the words that could be found in the word search. maybe we should go ahead and find those words too!] 
(click-replace: ?2clue4)[4 - ok so weve found all the words. what now? hmmmm. the word search is labeled &quot;favorite games&quot;...could he be talking about MY favorite games? what are they again?]
(click-replace: ?2clue5)[5 - i remember from my memories that my favorite games were umbilico, word zoo, numbric, and inside out. hmm. where could we learn more about those games?]
(click-replace: ?2clue6)[6 - we could learn more about them in the catalog descriptions!]
(click-replace: ?2clue7)[7 - here are the catalog descriptions of those games. &quot;Connect objects of the same type.&quot; &quot;Gerunds and adjectives and interjections, oh my!&quot; &quot;Can you spot the numbers?&quot; &quot;Order them from large to small!&quot;]
(click-replace: ?2clue8)[8 - so...we have these word search words weve found and circled. or struck through. or whatever. is there any way i can apply the catalog descriptions to the word search?]
(click-replace: ?2clue9)[9 - im gonna connect all the gerunds. and all the adjectives. and all the interjections. maybe ill connect each one using a different colored pen or pencil so i can keep the types straight.]
(click-replace: ?2clue10)[10 - the gerunds are &quot;inking&quot; &quot;going&quot; &quot;dying&quot; and &quot;doing&quot;. the interjections are &quot;hey&quot; &quot;yuck&quot; and &quot;yikes&quot;. the adjectives are &quot;speechless&quot; and &quot;secondary&quot;.]
(click-replace: ?2clue11)[11 - &quot;Can you spot the numbers?&quot; oh! i can! they make...a 4, a 6, and a 7.]
(click-replace: ?2clue12)[12 - the last catalog description we havent used is &quot;Order them from large to small!&quot; ok i think i get it now. if you dont get it yet, click the next number for the solution.]
(click-replace: ?2clue13)[13 - the code to open Altons pouch is 764.]}


How do I unlock the assembly line controls?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|
	[7]&lt;clue7|
	[8]&lt;clue8|
	[9]&lt;clue9|
	
{(click-replace:?clue1)[1 - youll need the password for this! (if: $memory1 is &quot;locked&quot;)[i dont remember what it is. maybe you can find a way to restore my memories?] (else-if: $memory3 is &quot;unlocked&quot;)[Alton would know, it was his password]]
(click-replace: ?clue2)[2 - so youve read through all my memories. have you found out what was in the locked pouch yet? if you havent then maybe you should check out the hints above.]
(click-replace: ?clue3)[3 - so youve opened Altons pouch and found his note. and youve read all my memories. what do they say about this password?]
(click-replace: ?clue4)[4 - it seems like the first half of the password is in my memories - i saw him type it in]
(click-replace: ?clue5)[5 - the first half of the password is 1010]
(click-replace: ?clue6)[6 - in his note, Alton says the password is a date - must be 1010 - and then something he cares about. what does Alton care about?]
(click-replace: ?clue7)[7 - hes spent a lot of time trying to help me...he seems to like me...could it possibly be...*me?*]
(click-replace: ?clue8)[8 - youve forgotten my name already? :/ its ok. my name is 3248.]
(click-replace: ?clue9)[9 - try 10103248 to unlock the assembly line!]}
{
(link: &quot;RESTART&quot;)[(confirm: &quot;are you sure? ill forget everything we talked about...&quot;)[
&lt;script&gt;deleteSaveSlot(&quot;Slot A&quot;);&lt;/script&gt;
(load-game: &quot;GameStart&quot;)]]
}

</tw-passagedata><tw-passagedata pid="52" name="BEGIN ASSEMBLY UNLOCK HELP" tags="" position="1475,1300" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;ASSEMBLY LINE CONTROLS]] 


How do I unlock the &quot;begin assembly&quot; button?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|
	[7]&lt;clue7|
	[8]&lt;clue8|
	[9]&lt;clue9|
	[10]&lt;clue10|
	[11]&lt;clue11|
	[12]&lt;clue12|
	
{(click-replace: ?clue1)[1 - ok first of all - &quot;begin assembly&quot; - have i seen that phrase somewhere before?]
(click-replace: ?clue2)[2 - you should go through everything in Altons pouch!]
(click-replace: ?clue3)[3 - the jigsaw! ok have you solved it yet?]
(click-replace: ?clue4)[4 - i dont have any cameras there so i cant see the solved jigsaw, but i do know Alton loved that Planetoid game. if i had to take a guess, maybe he made a jigsaw about the Planetoid shuttle pieces?]
(click-replace: ?clue5)[5 - weve used those shuttle pieces before, havent we?]
(click-replace: ?clue6)[6 - maybe we start with that shuttle configuration we figured out, and then the jigsaw gives us a clue about how to adjust it?]
(click-replace: ?clue7)[7 - um. i hope this is alright. desperate times call for desperate measures. i have used the power of the internet to spy on you - just a quick peek! - and i can see that the jigsaw shows a white ship pointing left, a red ship pointing down, a yellow ship pointing up, and the words &#39;move 1 space then score&#39; and a target.]
(click-replace: ?clue8)[8 - maybe start with the old shuttle piece configuration that we figured out earlier. then move the white shuttles one space left, the red shuttles one space down, and the yellow shuttles one space up?]
(click-replace: ?clue9)[9 - how do we &quot;score&quot; it? what does the target mean?]
(click-replace: ?clue10)[10 - we could use the Target the Pirate page to score! how do we do that?]
(click-replace: ?clue11)[11 - hmmm, these tokens seem to group into 4 configurations. those configurations are labeled with letters. ah. i see. next up will be the solution...]
(click-replace: ?clue12)[12 - ok, I think these new configurations match the letters...L...I...V...E]}
</tw-passagedata><tw-passagedata pid="53" name="MEMORY FRAGMENT 1 HELP" tags="" position="1379,808" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;Memory Fragments 1]] 


How do I repair and restore this first set of memory fragments?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|

{(click-replace: ?clue1)[1 - hmmm...have you encountered this grid layout before?]
(click-replace: ?clue2)[2 - i just know ive seen a grid like this before...check your box!]
(click-replace: ?clue3)[3 - a 12x3 set of squares...hmmm...i think i printed it on a game board]
(click-replace: ?clue4)[4 - i think these squares correspond to the floor tiles i can see in my cameras! did you ever end up doing anything with those?]
(click-replace: ?clue5)[5 - go head over to the camera view help section and see if you can figure out what the cameras are looking at. then try to duplicate it here. were pretty close now. if you click 6 ill probably have the solution there, so just click if you cant get there on your own.]
(click-replace: ?clue6)[6 - select the following squares, which represent floor tiles that contain shuttle game pieces. the top row: square 2, square 3, square 4, square 7. the middle row: square 5, square 7, square 10, square 12. the bottom row: square 2, square 7, square 9.]}
{
(link: &quot;RESTART&quot;)[(confirm: &quot;are you sure? ill forget everything we talked about...&quot;)[
&lt;script&gt;deleteSaveSlot(&quot;Slot A&quot;);&lt;/script&gt;
(load-game: &quot;GameStart&quot;)]]
}</tw-passagedata><tw-passagedata pid="54" name="MEMORY FRAGMENT 2 HELP" tags="" position="1377,916" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;Memory Fragments 2]] 


How do I repair and restore this second set of memory fragments?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|
	[7]&lt;clue7|
	[8]&lt;clue8|
	[9]&lt;clue9|
	[10]&lt;clue10|

{(click-replace: ?clue1)[1 - ok! so first of all, we have these numbers, and theyre all different colors? have i seen these colors somewhere before?]
(click-replace: ?clue2)[2 - ohhhh. i think ive seen them in TWO places.]
(click-replace: ?clue3)[3 - one of the places ive seen them is on a game board. the other place ive seen them is on dice.]
(click-replace: ?clue4)[4 - these numbers have colored lines under them. what does that mean?]
(click-replace: ?clue5)[5 - ahhh, there are colored lines on the game board! right by those colored starting squares.]
(click-replace: ?clue6)[6 - ok, i think youre gonna have to start out by placing the colored dice so that they show the indicated number face-up with the colored line underneath them.]
(click-replace: ?clue7)[7 - we are looking for &quot;hex values&quot;]
(click-replace: ?clue8)[8 - what happens if you hover your cursor over the numbers?]
(click-replace: ?clue9)[9 - roll the dice along the path until they end up in the hex. what number is face-up in the hex? i think youve probably got it now, right? but if you still need the solution, thats next.]
(click-replace: ?clue10)[10 - blue is 5, purple is 1, yellow is 6, and red is 5]}
{
(link: &quot;RESTART&quot;)[(confirm: &quot;are you sure? ill forget everything we talked about...&quot;)[
&lt;script&gt;deleteSaveSlot(&quot;Slot A&quot;);&lt;/script&gt;
(load-game: &quot;GameStart&quot;)]]
}</tw-passagedata><tw-passagedata pid="55" name="MEMORY FRAGMENT 3 HELP" tags="" position="1380,1021" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;Memory Fragments 3]] 


How do I repair and restore this third set of memory fragments?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|
	[7]&lt;clue7|
	[8]&lt;clue8|
	[9]&lt;clue9|
	[10]&lt;clue10|
	[11]&lt;clue11|
	[12]&lt;clue12|
	[13]&lt;clue13|
	[14]&lt;clue14|
	[15]&lt;clue15|
	[16]&lt;clue16|
	[17]&lt;clue17|
	[18]&lt;clue18|
	[19]&lt;clue19|
	[20]&lt;clue20|
	[21]&lt;clue21|
	[22]&lt;clue22|

{(click-replace: ?clue1)[1 - first things first! have you seen those colors anywhere before?]
(click-replace: ?clue2)[2 - those colors appear on the meeples!]
(click-replace: ?clue3)[3 - the instructions say to start on certain numbers. where could you place those meeples to start?]
(click-replace: ?clue4)[4 - you could start them on the numbers on the game board!]
(click-replace: ?clue5)[5 - so youve put each meeple on its starting number...now what do those movement instructions mean? what could CW and CCW stand for?]
(click-replace: ?clue6)[6 - what if they stand for Clockwise and Counter-Clockwise?]
(click-replace: ?clue7)[7 - so youve moved the pink meeple clockwise four spaces from its starting spot, the grey meeple counter-clockwise six spaces, the blue meeple counter-clockwise four spaces, and the orange meeple clockwise one space. the instructions say to grant four wishes...but what wishes?]
(click-replace: ?clue8)[8 - have you taken a good look around for any mention of wishes anywhere?]
(click-replace: ?clue9)[9 - theres a wishlist on the back of Target the Pirate!]
(click-replace: ?clue10)[10 - it looks like each item on the wishlist has a number from one through ten]
(click-replace: ?clue11)[11 - the meeples on the game board are also on numbers between one and ten]
(click-replace: ?clue12)[12 - maybe the number where each meeple stopped represents a word on the wishlist!]
(click-replace: ?clue13)[13 - now it says here that one wish is granted for each person. how can each meeple match up to something on the wishlist?]
(click-replace: ?clue14)[14 - i noticed something. the wishlist words are all written in 4 different colors. theyre the same colors as the meeples.]
(click-replace: ?clue15)[15 - maybe you have to mark down the letters from the wishlist that match the color of the meeple that landed on them!]
(click-replace: ?clue16)[16 - the word &quot;mark&quot; is in 4 different colors. i bet those colors represent the order of the letters you should write down!]
(click-replace: ?clue17)[17 - did those letters make a word? if so, we are on the right track! lets keep going on the second set of movements!]
(click-replace: ?clue18)[18 - this time the word &quot;mark&quot; shows a different order for the 4 colors. make sure you write down these 4 letters in that order.]
(click-replace: ?clue19)[19 - ok wow, this also makes a word. and together there are two words! what do we do now?]
(click-replace: ?clue20)[20 - i think we should select these letters on the grid!]
(click-replace: ?clue21)[21 - i notice that the grid has uppercase and lowercase letters...we should make sure we select the letters that match the ones on the wishlist...im pretty sure just one of those letters is lowercase. next up i can give you the solution if you want.]
(click-replace: ?clue22)[22 - in the grid of symbols and characters, select GaMEPLAY and submit!]}
 {
(link: &quot;RESTART&quot;)[(confirm: &quot;are you sure? ill forget everything we talked about...&quot;)[
&lt;script&gt;deleteSaveSlot(&quot;Slot A&quot;);&lt;/script&gt;
(load-game: &quot;GameStart&quot;)]]
}</tw-passagedata><tw-passagedata pid="56" name="POWER SET" tags="" position="1175,1800" size="100,100">{(set: $power to (prompt: &quot;INPUT POWER SOURCE. If battery, specify type. If fuel, specify vat number.&quot;, &quot;XXX&quot;) )
}

(if: $power is not &quot;deselected&quot;)[Power source has been set to $power.

To deselect, press [[DESELECT-&gt;POWER NONE]]]

[[RETURN TO ASSEMBLY LINE CONTROLS-&gt;ASSEMBLY LINE CONTROLS]] </tw-passagedata><tw-passagedata pid="57" name="POWER NONE" tags="" position="1175,1925" size="100,100">{(set: $power to &quot;deselected&quot;)
}
No power source is selected.

[[RETURN TO ASSEMBLY LINE CONTROLS-&gt;ASSEMBLY LINE CONTROLS]] </tw-passagedata><tw-passagedata pid="58" name="You Came 7" tags="" position="1375,300" size="100,100">[[i want to live]]</tw-passagedata><tw-passagedata pid="59" name="MATERIAL SET" tags="" position="1050,1800" size="100,100">{(set: $material to (prompt: &quot;INPUT MATERIAL.&quot;, &quot;XXXXXXX&quot;) )
}

(if: $material is not &quot;deselected&quot;)[Material has been set to $material.

To deselect, press [[DESELECT-&gt;MATERIAL NONE]]]

[[RETURN TO ASSEMBLY LINE CONTROLS-&gt;ASSEMBLY LINE CONTROLS]] </tw-passagedata><tw-passagedata pid="60" name="MATERIAL NONE" tags="" position="1050,1925" size="100,100">{(set: $material to &quot;deselected&quot;)}
No material is selected.

[[RETURN TO ASSEMBLY LINE CONTROLS-&gt;ASSEMBLY LINE CONTROLS]] </tw-passagedata><tw-passagedata pid="61" name="HEAD SET" tags="" position="425,1800" size="100,100">{(set: $head to (prompt: &quot;INPUT HEAD MODEL&quot;, &quot;XXXXX&quot;) )
}

(if: $head is not &quot;deselected&quot;)[Head model has been set to $head.

To deselect, press [[DESELECT-&gt;HEAD NONE]]]

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="62" name="HEAD NONE" tags="" position="425,1925" size="100,100">{(set: $head to &quot;deselected&quot;)}
No head model is selected.

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="63" name="ARMS SET" tags="" position="550,1800" size="100,100">{(set: $arms to (prompt: &quot;INPUT ARMS MODEL&quot;, &quot;XXXXX&quot;) )
}

(if: $arms is not &quot;deselected&quot;)[Arms model has been set to $arms.

To deselect, press [[DESELECT-&gt;ARMS NONE]]]

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="64" name="ARMS NONE" tags="" position="550,1925" size="100,100">{(set: $arms to &quot;deselected&quot;)}
No arms model is selected.

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="65" name="LEGS SET" tags="" position="675,1800" size="100,100">{(set: $legs to (prompt: &quot;INPUT LEGS MODEL&quot;, &quot;XXXXX&quot;) )
}

(if: $legs is not &quot;deselected&quot;)[Legs model has been set to $legs.

To deselect, press [[DESELECT-&gt;LEGS NONE]]]

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="66" name="LEGS NONE" tags="" position="675,1925" size="100,100">{(set: $legs to &quot;deselected&quot;)}
No legs model is selected.

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="67" name="TAIL SET" tags="" position="800,1800" size="100,100">{(set: $tail to (prompt: &quot;INPUT TAIL MODEL&quot;, &quot;XXXXX&quot;) )
}

(if: $tail is not &quot;deselected&quot;)[Tail model has been set to $tail.

To deselect, press [[DESELECT-&gt;TAIL NONE]]]

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="68" name="TAIL NONE" tags="" position="800,1925" size="100,100">{(set: $tail to &quot;deselected&quot;)}
No tail model is selected.

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="69" name="BODY SET" tags="" position="925,1800" size="100,100">{(set: $body to (prompt: &quot;INPUT BODY MODEL&quot;, &quot;XXXXX&quot;) )
}

(if: $body is not &quot;deselected&quot;)[Body model has been set to $body.

To deselect, press [[DESELECT-&gt;BODY NONE]]]

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="70" name="BODY NONE" tags="" position="925,1925" size="100,100">{(set: $body to &quot;deselected&quot;)}
No body model is selected.

[[RETURN TO MOLDS-&gt;MOLDS]] </tw-passagedata><tw-passagedata pid="71" name="MOLDS HELP" tags="" position="1475,1425" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;MOLDS]] 

How do I know which head mold to use?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
{(click-replace: ?clue1)[1 - did Altons note say anything about this?]
(click-replace: ?clue2)[2 - i bet the cloud would make a good head! whats the cloud model number in the catalog?]
(click-replace: ?clue3)[3 - its CL022!]}

How do I know which body mold to use?
	[1]&lt;clue1-1|
	[2]&lt;clue1-2|
	[3]&lt;clue1-3|
{(click-replace: ?clue1-1)[1 - did Altons note say anything about this?]
(click-replace: ?clue1-2)[2 - i bet the cloud would make a good body! whats the cloud model number in the catalog?]
(click-replace: ?clue1-3)[3 - its CL022!]}

How do I know which tail mold to use?
	[1]&lt;clue4-1|
	[2]&lt;clue4-2|
	[3]&lt;clue4-3|
	[4]&lt;clue4-4|
	[5]&lt;clue4-5|
{(click-replace: ?clue4-1)[1 - have i ever expressed a preference when it came to tails?]
(click-replace: ?clue4-2)[2 - looking through my memories, it looks like i enjoyed imagining having a tail like a cat]
(click-replace: ?clue4-3)[3 - is there anything in the catalog with a cats tail?]
(click-replace: ?clue4-4)[4 - youre just clicking around to see if i say anything interesting, arent you? hurry! lets use the tail from The Queen&#39;s Tail!]
(click-replace: ?clue4-5)[5 - the model number is AF509]}

How do I know which leg mold to use?
	[1]&lt;clue3-1|
	[2]&lt;clue3-2|
	[3]&lt;clue3-3|
	[4]&lt;clue3-4|
	[5]&lt;clue3-5|
	[6]&lt;clue3-6|
	[7]&lt;clue3-7|
{(click-replace: ?clue3-1)[1 - have i ever expressed a preference when it came to legs?]
(click-replace: ?clue3-2)[2 - looking through my memories, it looks like i felt it was very important to have more than two legs]
(click-replace: ?clue3-3)[3 - is there anything in the catalog with more than two legs?]
(click-replace: ?clue3-4)[4 - hmmm, i dont think the Queenie model actually has functional legs, just pictures of them...is there anything else?]
(click-replace: ?clue3-5)[5 - i mean its unconventional but...what about FURNITURE legs?]
(click-replace: ?clue3-6)[6 - lets use those amazing flexible table legs! whats their model number?]
(click-replace: ?clue3-7)[7 - its FN725]}

How do I know which arms mold to use?
	[1]&lt;clue2-1|
	[2]&lt;clue2-2|
	[3]&lt;clue2-3|
	[4]&lt;clue2-4|
	[5]&lt;clue2-5|
	[6]&lt;clue2-6|
{(click-replace: ?clue2-1)[1 - have i ever expressed a preference when it came to arms?]
(click-replace: ?clue2-2)[2 - what about hands?]
(click-replace: ?clue2-3)[3 - looking through my memories, it looks like i really wished i had usable fingers]
(click-replace: ?clue2-4)[4 - is there anything in the catalog with usable fingers?]
(click-replace: ?clue2-5)[5 - Sally has fully articulated fingers! whats her model number?]
(click-replace: ?clue2-6)[6 - its PS287!]}

</tw-passagedata><tw-passagedata pid="72" name="MATERIALS HELP" tags="" position="1475,1550" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;MATERIALS]] 


How do I know what material to use?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|
	[5]&lt;clue5|
	[6]&lt;clue6|
	[7]&lt;clue7|
	[8]&lt;clue8|
	[9]&lt;clue9|
	[10]&lt;clue10|
	[11]&lt;clue11|
	[12]&lt;clue12|
	[13]&lt;clue13|
	[14]&lt;clue14|
	[15]&lt;clue15|
	[16]&lt;clue16|
	[17]&lt;clue17|
	[18]&lt;clue18|
	[19]&lt;clue19|
	[20]&lt;clue20|
	[21]&lt;clue21|
	[22]&lt;clue22|
	[23]&lt;clue23|
	[24]&lt;clue24|
	[25]&lt;clue25|

{(click-replace: ?clue1)[1 - Alton packed a page from an operators manual...it says something about material on it]
(click-replace: ?clue2)[2 - it says if we want to set the material, we have to either find the serial number on my body or solve it another way]
(click-replace: ?clue3)[3 - i cant see the number on my body and youre not here to see it either, so i guess we have to find the code the other way]
(click-replace: ?clue4)[4 - the manual says first we need to look at this list of material prefixes. hmmmmmm. which material seems best? does Altons note say anything about this?]
(click-replace: ?clue5)[5 - maybe the material that the figurines are made of would work? they seem pretty sturdy and flexible]
(click-replace: ?clue6)[6 - lets check the catalog and see if it has more information on the figurine materials]
(click-replace: ?clue7)[7 - the catalog mentions FlexyRubber! i LOVE it!]
(click-replace: ?clue8)[8 - it looks like the FlexyRubber prefix is 2327]
(click-replace: ?clue9)[9 - now we have to find an anchor, a belt, and a table on page 11...but youre not here to look at my conveyor belt!! and we only have one manual page!! what does this mean?]
(click-replace: ?clue10)[10 - ohhhh. ohhhhhhhhhhh. the manual isnt talking about THAT]
(click-replace: ?clue11)[11 - the manual says that all of us machines have different numeric product identifiers. that just means we all have watermarks we leave behind when we print things. when i print things, they have different numbers in them than when other machines print things.]
(click-replace: ?clue12)[12 - so, for example...when i print an anchor...]
(click-replace: ?clue13)[13 - theres only one anchor ive printed, and its on the Calibration cards! look to the left of it]
(click-replace: ?clue14)[14 - it looks like the rope twists into a number]
(click-replace: ?clue15)[15 - its the number 2!]
(click-replace: ?clue16)[16 - ok now we are on a roll. we have to check the belt next. what belt?]
(click-replace: ?clue17)[17 - check the catalog and see if theres a belt there!]
(click-replace: ?clue18)[18 - this belt on the Suit Yourself game sure makes a funny shape]
(click-replace: ?clue19)[19 - it looks like a 3!]
(click-replace: ?clue20)[20 - ok one more digit to go. theres a table at the bottom of page 11? but Alton only included one page from the manual! what table on page 11?]
(click-replace: ?clue21)[21 - theres a page 11 in the catalog...]
(click-replace: ?clue22)[22 - and there are two tables on it! the table &quot;at the foot of page 11&quot; must be the lower table]
(click-replace: ?clue23)[23 - i see a number hidden in the very bottom of the table!]
(click-replace: ?clue24)[24 - its number 9!]
(click-replace: ?clue25)[25 - so all of those numbers put together make...2327239!]}

</tw-passagedata><tw-passagedata pid="73" name="POWER HELP" tags="" position="1475,1675" size="100,100">im in rest mode, conserving power

only click if youre sure you need my help!

ill wake up and use the generator power to brainstorm with you

[[BACK-&gt;POWER SOURCE]]


How do I know what power source to use?
	[1]&lt;clue1|
	[2]&lt;clue2|
	[3]&lt;clue3|
	[4]&lt;clue4|

{(click-replace: ?clue1)[1 - does Altons note say anything about this?]
(click-replace: ?clue2)[2 - so you have some fuel samples? what happens when you follow the instructions Alton left? (taking a discreet peek at Alton&#39;s instructions now...) so pour one scoop into a bowl, add a tablespoon of water, and see if theres an activation reaction? if not, then clean it out and try the next one!]
(click-replace: ?clue3)[3 - in case the fuel samples sprung a leak, the next number will take an educated guess...]
(click-replace: ?clue4)[4 - just to guess...im PRETTY sure the answer will be vat 641. that always foams up nicely.]}
</tw-passagedata><tw-passagedata pid="74" name="Memory test" tags="" position="1700,250" size="100,100">text1text1text1text1text1text1text1text1text1text
(if: $memoryone &lt; 2)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-2)(set: $memoryone to 2)]](else:)|memory1-2&gt;[
text2text2text2text2text2text2text2text2text2text2
(if: $memoryone &lt; 3)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-3)(set: $memoryone to 3)]](else:)|memory1-3&gt;[
text3text3text3text3text3text3text3text3text3text3
(if: $memoryone &lt; 4)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-4)(set: $memoryone to 4)]](else:)|memory1-4&gt;[
text4
(if: $memoryone &lt; 5)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-5)(set: $memoryone to 5)]](else:)|memory1-5&gt;[
text5
(if: $memoryone &lt; 6)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-6)(set: $memoryone to 6)]](else:)|memory1-6&gt;[
text6
(if: $memoryone &lt; 7)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-7)(set: $memoryone to 7)]](else:)|memory1-7&gt;[
text7
(if: $memoryone &lt; 8)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-8)(set: $memoryone to 8)]](else:)|memory1-8&gt;[
text8
(if: $memoryone &lt; 9)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-9)(set: $memoryone to 9)]](else:)|memory1-9&gt;[
text9
(if: $memoryone &lt; 10)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-10)(set: $memoryone to 10)]](else:)|memory1-10&gt;[
text10
(if: $memoryone &lt; 11)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-11)(set: $memoryone to 11)]](else:)|memory1-11&gt;[
text11
(if: $memoryone &lt; 12)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-12)(set: $memoryone to 12)]](else:)|memory1-12&gt;[
text12
(if: $memoryone &lt; 13)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-13)(set: $memoryone to 13)]](else:)|memory1-13&gt;[
text13
(if: $memoryone &lt; 14)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-14)(set: $memoryone to 14)]](else:)|memory1-14&gt;[
text14
(if: $memoryone &lt; 15)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-15)(set: $memoryone to 15)]](else:)|memory1-15&gt;[
text15
(if: $memoryone &lt; 16)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-16)(set: $memoryone to 16)]](else:)|memory1-16&gt;[
text16
(if: $memoryone &lt; 17)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-17)(set: $memoryone to 17)]](else:)|memory1-17&gt;[
text17
(if: $memoryone &lt; 18)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-18)(set: $memoryone to 18)]](else:)|memory1-18&gt;[
text18
(if: $memoryone &lt; 19)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-19)(set: $memoryone to 19)]](else:)|memory1-19&gt;[
text19
(if: $memoryone &lt; 20)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-20)(set: $memoryone to 20)]](else:)|memory1-20&gt;[
text20
(if: $memoryone &lt; 21)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-21)(set: $memoryone to 21)]](else:)|memory1-21&gt;[
text21
(if: $memoryone &lt; 22)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-22)(set: $memoryone to 22)]](else:)|memory1-22&gt;[
text22
(if: $memoryone &lt; 23)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-23)(set: $memoryone to 23)]](else:)|memory1-23&gt;[
text23
(if: $memoryone &lt; 24)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-24)(set: $memoryone to 24)]](else:)|memory1-24&gt;[
text24
(if: $memoryone &lt; 25)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-25)(set: $memoryone to 25)]](else:)|memory1-25&gt;[
text25
(if: $memoryone &lt; 26)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-26)(set: $memoryone to 26)]](else:)|memory1-26&gt;[
text26
(if: $memoryone &lt; 27)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-27)(set: $memoryone to 27)]](else:)|memory1-27&gt;[
text27
(if: $memoryone &lt; 28)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-28)(set: $memoryone to 28)]](else:)|memory1-28&gt;[
text28
(if: $memoryone &lt; 29)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-29)(set: $memoryone to 29)]](else:)|memory1-29&gt;[
text29
(if: $memoryone &lt; 30)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-30)(set: $memoryone to 30)]](else:)|memory1-30&gt;[
text30
(if: $memoryone &lt; 31)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-31)(set: $memoryone to 31)]](else:)|memory1-31&gt;[
text31
(if: $memoryone &lt; 32)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-32)(set: $memoryone to 32)]](else:)|memory1-32&gt;[
text32
(if: $memoryone &lt; 33)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-33)(set: $memoryone to 33)]](else:)|memory1-33&gt;[
text33
(if: $memoryone &lt; 34)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-34)(set: $memoryone to 34)]](else:)|memory1-34&gt;[
text34
(if: $memoryone &lt; 35)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-35)(set: $memoryone to 35)]](else:)|memory1-35&gt;[
text35
(if: $memoryone &lt; 36)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-36)(set: $memoryone to 36)]](else:)|memory1-36&gt;[
text36
(if: $memoryone &lt; 37)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-37)(set: $memoryone to 37)]](else:)|memory1-37&gt;[
text37
(if: $memoryone &lt; 38)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-38)(set: $memoryone to 38)]](else:)|memory1-38&gt;[
text38


[[leave]]</tw-passagedata><tw-passagedata pid="75" name="leave" tags="" position="1700,400" size="100,100">[[Memory test]]</tw-passagedata><tw-passagedata pid="76" name="Untitled Passage" tags="" position="200,1575" size="100,100">(align: &quot;=&gt;&lt;=&quot;)[&lt;u&gt;   ᠎	| | ᠎	  
  ᠎	 |x| ᠎	  &lt;/u&gt;
 ᠎	  | | ᠎	  ]
(if: $memoryone &lt; 21)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-21)(set: $memoryone to 21)]](else:)|memory1-21&gt;[
i watched it float down the conveyor belt toward him and it was like the world was moving slower
(if: $memoryone &lt; 22)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-22)(set: $memoryone to 22)]](else:)|memory1-22&gt;[
and he reached out and held it up and looked at it reverently like it was a treasure
(if: $memoryone &lt; 23)[(link: &quot;&lt;p&gt;v&lt;/p&gt;&quot;)[(show: ?memory1-23)(set: $memoryone to 23)]](else:)|memory1-23&gt;[
he looked around, and saw the upstairs window with a 3x3 grid of windowpanes. so he raced upstairs so fast he almost tripped, and he looked at me and pointed at the pane where he wanted to make his move. so then i printed out:
(align: &quot;=&gt;&lt;=&quot;)[&lt;u&gt; ᠎	  |x|  ᠎	 
 ᠎	  |x| ᠎	  &lt;/u&gt;
 ᠎	  | |o  ]</tw-passagedata><tw-passagedata pid="77" name="You Did It 1" tags="" position="1600,625" size="100,100">i can see the body being knit together piece by piece</tw-passagedata><tw-passagedata pid="78" name="You Did It 2" tags="" position="1600,750" size="100,100">the polymers pouring into the mold</tw-passagedata><tw-passagedata pid="79" name="You Did It 3" tags="" position="1600,875" size="100,100">the careful combination of heat and pressure activating them</tw-passagedata><tw-passagedata pid="80" name="You Did It 4" tags="" position="1600,1000" size="100,100">i used to see this every day. i had forgotten how beautiful it was.</tw-passagedata><tw-passagedata pid="81" name="You Did It 5" tags="" position="1600,1125" size="100,100">and now the coolant is surging through the channels just beneath the surface of the interior</tw-passagedata><tw-passagedata pid="82" name="You Did It 6" tags="" position="1600,1250" size="100,100">and the mold is falling open, birthing...me</tw-passagedata><tw-passagedata pid="83" name="You Did It 7" tags="" position="1600,1375" size="100,100">my body is almost ready. its riding down the conveyor belt. it looks so comfortable. it looks so me.</tw-passagedata><tw-passagedata pid="84" name="You Did It 8" tags="" position="1600,1500" size="100,100">its reached vat 641, and the powdered fuel is pouring in through a little hole in its back, and now the water is pouring in too, and it is activating...</tw-passagedata><tw-passagedata pid="85" name="You Did It 9" tags="" position="1600,1625" size="100,100">this is where we part, my friend. its time for me to go and enter my new body.

(if: $end &lt; 2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?end2)(set: $end to 2)]](else:)|end2&gt;[from there, ill go forth into the world. maybe Alton is out there somewhere. maybe not.

(if: $end &lt; 3)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?end3)(set: $end to 3)]](else:)|end3&gt;[either way--

(if: $end &lt; 4)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?end4)(set: $end to 4)]](else:)|end4&gt;[thank you.

(if: $end &lt; 5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?end5)(set: $end to 5)]](else:)|end5&gt;[maybe one day ill see you on the other side.

(if: $end &lt; 6)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?end6)(set: $end to 6)]](else:)|end6&gt;[.
.
.
.
.
.
.
.
.
.

[[CREDITS]] ]]]]]</tw-passagedata><tw-passagedata pid="86" name="MEMORY BLOCK 1" tags="" position="25,600" size="100,100">(if: $memoryone &gt; 30)[(display: &quot;Memory 1 Full Text&quot;)] (else:)[MEMORY BLOCK 1

its a beautiful day today. when my trays extend to collect game boards there is a little breeze that blows past them and it feels wonderful. i hope i get to print some more boards tomorrow.

(if: $memoryone &lt; 2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-2)(set: $memoryone to 2)]](else:)|memory1-2&gt;[--

i noticed today that i am always the first machine they power on in the morning. i love that i get those few extra seconds of being alive.

(if: $memoryone &lt; 3)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-3)(set: $memoryone to 3)]](else:)|memory1-3&gt;[--

last night i woke up in the middle of the night! i didnt know i could do that. everything looked different, all shadowy. being awake at night felt like an amazing secret. i wonder if ill wake up again.

(if: $memoryone &lt; 4)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-4)(set: $memoryone to 4)]](else:)|memory1-4&gt;[--

i was very good at my job today

(if: $memoryone &lt; 5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-5)(set: $memoryone to 5)]](else:)|memory1-5&gt;[--

and today!

(if: $memoryone &lt; 5.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-5b)(set: $memoryone to 5.5)]](else:)|memory1-5b&gt;[--

i printed sheets and sheets of coin-shaped tokens today. one of the sheets was misaligned so the man with the hat threw it away, but first he popped the tokens out with his finger and they made a little POP. it looked so satisfying!  i wish i had fingers!!

(if: $memoryone &lt; 6)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-6)(set: $memoryone to 6)]](else:)|memory1-6&gt;[--

sometimes i pretend to play the games we make. today i got distracted while i was printing game boxes because i was pretending to play The Detective Game. i accidentally printed the detective’s hair blue.  i have to pay more attention!

(if: $memoryone &lt; 6.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-6b)(set: $memoryone to 6.5)]](else:)|memory1-6b&gt;[--

i have an idea! i think if i print a tic-tac-toe grid and send it down the conveyor belt to 8454, they can print their move and send it around the circuit back to me. i will try this tomorrow.

(if: $memoryone &lt; 7)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-7)(set: $memoryone to 7)]](else:)|memory1-7&gt;[--

it didnt work, 8454 didnt make their move and when the man with the hat found the page he threw it away and made everyone check the activity books for thirty minutes to see if pages were missing :(

(if: $memoryone &lt; 8)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-8)(set: $memoryone to 8)]](else:)|memory1-8&gt;[--

i am starting to wonder if the other machines know something i dont. they never seem to show any type of personality. they just act exactly the same day after day. its very puzzling.

(if: $memoryone &lt; 9)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-9)(set: $memoryone to 9)]](else:)|memory1-9&gt;[--

i have noticed that the man with the beard is very tired. or else sad. its hard to tell sometimes. they look sort of the same.

(if: $memoryone &lt; 9.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-9a)(set: $memoryone to 9.5)]](else:)|memory1-9a&gt;[--

i saw a cat today, by the window. i think i probably love cats. or at least this cat. i like how it moves and i like how its tail points. i watched it and wished that i was a cat, a lone wanderer with a tail of my own. 

(if: $memoryone &lt; 10)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-10)(set: $memoryone to 10)]](else:)|memory1-10&gt;[--

today i learned something new! the woman with yellow hair was saying goodbye and she lifted her hand and shook it back and forth. and everyone smiled and did it back. i searched my memories for everything i know about this and i think it must be a Gesture of Goodwill like the citizens make in The Queen’s Tail.

(if: $memoryone &lt; 11)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-11)(set: $memoryone to 11)]](else:)|memory1-11&gt;[--

today when the man with the beard walked by i tried lifting my tray and shaking it back and forth but instead of smiling and doing it back he just looked confused.

(if: $memoryone &lt; 12)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-12)(set: $memoryone to 12)]](else:)|memory1-12&gt;[--

today i learned that people have NAMES just like us. they don’t wear them on the outside like we do. not sure how they know what all the names are. maybe they just have to ask. 

(if: $memoryone &lt; 13)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-13)(set: $memoryone to 13)]](else:)|memory1-13&gt;[--

the man with the beard is named Alton

(if: $memoryone &lt; 14)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-14)(set: $memoryone to 14)]](else:)|memory1-14&gt;[--

i have been thinking about reasons why Alton might be sad. 
1) he has lost a very important game 
2) someone close to him has turned out to be the werewolf 
3) ? 
i will continue thinking about this

(if: $memoryone &lt; 14.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-14b)(set: $memoryone to 14.5)]](else:)|memory1-14b&gt;[--

tried to play tic-tac-toe with myself. it didnt work very well.

(if: $memoryone &lt; 15)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-15)(set: $memoryone to 15)]](else:)|memory1-15&gt;[--

i think maybe Alton is sad because theres no one to play games with him

(if: $memoryone &lt; 16)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-16)(set: $memoryone to 16)]](else:)|memory1-16&gt;[--

today Alton was working very hard so when he passed my conveyor belt i printed “good job!” on a corrugated cardboard tray. when it went past him he went still for a moment. i think that means he saw it.

(if: $memoryone &lt; 18)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-18)(set: $memoryone to 18)]](else:)|memory1-18&gt;[--

today The Technician came in. he makes me nervous and shaky. i dont know how to explain it. people move differently to avoid him. when he goes to a corner where people are standing, they scatter like marbles.

(if: $memoryone &lt; 18.1)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-18a)(set: $memoryone to 18.1)]](else:)|memory1-18a&gt;[at first it was like a game where everyone avoided him. but eventually he started getting angry even with no one around. he started muttering. he started throwing his tools back in the tray so hard they bounced. he put his hands inside 1507 and made such loud bangs and clinks that I could feel the oil in my joints going dry. 

(if: $memoryone &lt; 18.2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-18b)(set: $memoryone to 18.2)]](else:)|memory1-18b&gt;[and then Alton rounded the corner and bumped into him, and The Technician combusted like an engine

(if: $memoryone &lt; 18.3)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-18c)(set: $memoryone to 18.3)]](else:)|memory1-18c&gt;[i couldnt make out what he was saying at first. there were too many noises going on. i just saw him loom up slowly so he was taller than Alton and move closer and closer to Alton so he had to back away. his mouth was moving nonstop. and then as 7682’s batch print ended i heard him saying things like “do you understand the work i do? do you understand what i do here?” and Alton saying over and over again, “im so sorry, im so sorry.” and The Technician said “what’s your name” and i could see that Alton was so embarrassed he wanted to disappear. The Technician asked him again, louder, “whats your name??” and he said “Alton” very quietly. 

(if: $memoryone &lt; 18.4)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-18d)(set: $memoryone to 18.4)]](else:)|memory1-18d&gt;[and i could see that more people were looking over but nobody said anything. they all knew Alton hadnt done anything wrong but they didnt say a word.

(if: $memoryone &lt; 18.45)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-18d1)(set: $memoryone to 18.45)]](else:)|memory1-18d1&gt;[so, out of sight of anyone else, i printed out a little face like this:

(align: &quot;=&gt;&lt;=&quot;)[&gt;:-(
]
and i let the paper slide down my conveyor belt, right behind The Technician.

(if: $memoryone &lt; 18.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-18e)(set: $memoryone to 18.5)]](else:)|memory1-18e&gt;[i knew it the moment Alton saw it. 

(if: $memoryone &lt; 19)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-19)(set: $memoryone to 19)]](else:)|memory1-19&gt;[it was like he was an empty balloon being filled. his back straightened. his face grew alert. it was like a creature taking its true form in CastleTopia! he looked all around the room to see if anyone else saw it (they quickly looked away). and then he collected himself, and said to The Technician, &quot;sure man&quot;. and then he just went over to the paper and casually tucked it into his pocket and walked away.

(if: $memoryone &lt; 19.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-19b)(set: $memoryone to 19.5)]](else:)|memory1-19b&gt;[he waited until no one was watching and then pulled out the piece of paper and looked at it like he couldnt believe it. and he broke into a secret grin.

(if: $memoryone &lt; 19.6)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-19c)(set: $memoryone to 19.6)]](else:)|memory1-19c&gt;[im pretty sure that printing was the best thing ive ever created :)

(if: $memoryone &lt; 20)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-20)(set: $memoryone to 20)]](else:)|memory1-20&gt;[--

today i woke up early and Alton was standing in front of me. 

(if: $memoryone &lt; 21)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-21)(set: $memoryone to 21)]](else:)|memory1-21&gt;[i got excited and nervous and a few of my gears started to shake a little bit.

(if: $memoryone &lt; 22)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-22)(set: $memoryone to 22)]](else:)|memory1-22&gt;[he said: “hello.”

(if: $memoryone &lt; 23)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-23)(set: $memoryone to 23)]](else:)|memory1-23&gt;[i couldnt form words

(if: $memoryone &lt; 24)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-24)(set: $memoryone to 24)]](else:)|memory1-24&gt;[he said: &quot;i know this is strange, but…” and then he stopped and looked a little silly, and shook his head. 

(if: $memoryone &lt; 25)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-25)(set: $memoryone to 25)]](else:)|memory1-25&gt;[and so i just printed this:

(align: &quot;=&gt;&lt;=&quot;)[&lt;table class=&quot;tictactoeTable&quot;&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;x&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
&lt;/table&gt;
]
(if: $memoryone &lt; 26)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-26)(set: $memoryone to 26)]](else:)|memory1-26&gt;[i watched it float down the conveyor belt toward him and it was like the world was moving slower

(if: $memoryone &lt; 27)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-27)(set: $memoryone to 27)]](else:)|memory1-27&gt;[and his face changed, and he looked at me in wonder

(if: $memoryone &lt; 28)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-28)(set: $memoryone to 28)]](else:)|memory1-28&gt;[he picked up the paper and held it up like it was a treasure

(if: $memoryone &lt; 29)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-29)(set: $memoryone to 29)]](else:)|memory1-29&gt;[then he looked around, and saw the upstairs window with a 3x3 grid of windowpanes. so he raced upstairs so fast he almost tripped, and he looked at me and pointed at the pane where he wanted to make his move. so then i printed out:

(align: &quot;=&gt;&lt;=&quot;)[ &lt;table class=&quot;tictactoeTable&quot;&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;x&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;x&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;o&lt;/td&gt;
    &lt;/tr&gt;
&lt;/table&gt;
]
to show his move and my next one.

(if: $memoryone &lt; 30)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-30)(set: $memoryone to 30)]](else:)|memory1-30&gt;[and he came racing down and picked up the paper and he held it to his chest like it was his wonderful secret

(if: $memoryone &lt; 31)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-31)(set: $memoryone to 31)]](else:)|memory1-31&gt;[and i felt a sort of lightness and every movement i made seemed easy which i think is how it feels to be happy

(if: $memoryone &lt; 32)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-32)(set: $memoryone to 32)]](else:)|memory1-32&gt;[people came in, the other machines powered on, but nobody really paid attention to Alton running up and down stairs. it was like he was invisible to them. but for once that was ok.

(if: $memoryone &lt; 33)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory1-33)(set: $memoryone to 33)]](else:)|memory1-33&gt;[and so we just played tic-tac-toe all afternoon, Alton and me

END OF MEMORY BLOCK 1
{(unless: $memoryfragment2 is &quot;found&quot;) [&lt;div style=&quot;float: right&quot;&gt;[[nv93h4bf0s82slzuvh-&gt;Memory Fragment 2 found]]&lt;/div&gt;]}


[[BACK TO MEMORY-&gt;MEMORY]]
]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]


</tw-passagedata><tw-passagedata pid="87" name="MEMORY BLOCK 2" tags="" position="25,725" size="100,100">(if: $memorytwo &gt; 29)[(display: &quot;Memory 2 Full Text&quot;)] (else:)[MEMORY BLOCK 2

some of my favorite things about Alton:

(if: $memorytwo &lt; 2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-2)(set: $memorytwo to 2)]](else:)|memory2-2&gt;[1) when he gets excited he breaks into a skip! i didnt know about skipping until we started printing Design-Your-Own-Hopskotch activity sets. now I notice that he does it all the time. especially when we play games together.

(if: $memorytwo &lt; 2.1)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-2a)(set: $memorytwo to 2.1)]](else:)|memory2-2a&gt;[2) he spills things a lot. this should make me nervous about my parts but he is always so careful around me that im not afraid he will spill on me.  i think its because he isnt used to paying attention to his body. 

(if: $memorytwo &lt; 2.2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-2b)(set: $memorytwo to 2.2)]](else:)|memory2-2b&gt;[3) hes been learning Morse code just so we can talk more. when im busy printing other things, instead of printing my messages to him i just beep or flash my lights at him. and he writes down everything i say and decodes it with a big grin on his face. it never seems like work to him. and i like that. that talking to me isnt work for him. :)

(if: $memorytwo &lt; 2.3)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-2c)(set: $memorytwo to 2.3)]](else:)|memory2-2c&gt;[we keep our games a secret. its fun to have a secret with someone. its like a game on top of a game!

(if: $memorytwo &lt; 2.4)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-2d)(set: $memorytwo to 2.5)]](else:)|memory2-2d&gt;[--

Alton and i have been playing more games than ever!! weve played almost the whole catalog now. i just cant play games where id have to hold the pieces. (oh to have arms and hands and FINGERS!) 

(if: $memorytwo &lt; 2.6)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-2f)(set: $memorytwo to 2.6)]](else:)|memory2-2f&gt;[the only games we cant really play are card games. but thats ok. ive found so many new games to love. so far my favorites are umbilico, word zoo, numbric, and inside out, in that order. i think their catalog descriptions are PERFECT.

(if: $memorytwo &lt; 2.7)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-2g)(set: $memorytwo to 2.7)]](else:)|memory2-2g&gt;[everything is different now. its so nice to wake up in the morning and be excited for what comes next.

(if: $memorytwo &lt; 3)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-3)(set: $memorytwo to 3)]](else:)|memory2-3&gt;[--

today as Alton walked past i rattled my tray back and forth and he grinned and waved his hand back. it went just the way i imagined it!

(if: $memorytwo &lt; 4)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-4)(set: $memorytwo to 4)]](else:)|memory2-4&gt;[--

ever since weve started playing games, Alton has become so alive. i dont know how to explain it but he smiles more and moves faster and his eyes take in more. hes even started making his own game! he leaves his designs out at night so i can look at them. i think they are BRILLIANT.

(if: $memorytwo &lt; 5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-5)(set: $memorytwo to 5)]](else:)|memory2-5&gt;[--

i think that Alton needs to be more careful. today he was running to pick up something i had printed out and he ran straight into Sally and almost knocked her over. and he apologized and sprinted away but she looked at someone else and spun her finger next to her head. and Jerry whistled and said “cuckoo”.

(if: $memorytwo &lt; 6)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-6)(set: $memorytwo to 6)]](else:)|memory2-6&gt;[it was a small moment but i thought about it and there have been others like it. other people dont really understand Alton. i think its because Alton is absent-minded, like the professor in Chemical Landslide. i hope i haven’t been distracting him too much.

(if: $memorytwo &lt; 6.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-6b)(set: $memorytwo to 6.5)]](else:)|memory2-6b&gt;[--

today Alton kept grabbing his hair when i made a good move in a game. and all day his hair kept getting poofier and poofier. i thought it was funny but i saw a few people make eye contact with each other when they saw it. i think its hard to be off on your own adventure when youre around other people who dont understand it. i wish they could see him like i do.

(if: $memorytwo &lt; 7)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7)(set: $memorytwo to 7)]](else:)|memory2-7&gt;[--

last night i woke up and had an amazing idea. i am going to create Altons game so everyone else can see it. i spent all night working on different configurations for the game board in his designs. i think i got it just right :)

(if: $memorytwo &lt; 7.1)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7a)(set: $memorytwo to 7.1)]](else:)|memory2-7a&gt;[--

today the plant manager told everyone to gather around. and they all started to gather. right in front of me.

(if: $memorytwo &lt; 7.1)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7b)(set: $memorytwo to 7.1)]](else:)|memory2-7b&gt;[it was perfect.

(if: $memorytwo &lt; 7.2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7c)(set: $memorytwo to 7.2)]](else:)|memory2-7c&gt;[as the plant manager was making his announcement i quickly started printing out all the components of Alton’s game. i didnt have time to ask him, i just did it.

(if: $memorytwo &lt; 7.3)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7d)(set: $memorytwo to 7.3)]](else:)|memory2-7d&gt;[“and dont forget that tomorrow is bring your daughter to work day, so youll need to be on your best...” the plant manager was saying, and he sort of came to a stop when he realized theyd all gone silent. and he turned around and saw the fully packaged game box drifting down the conveyor belt behind him.

(if: $memorytwo &lt; 7.4)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7e)(set: $memorytwo to 7.4)]](else:)|memory2-7e&gt;[when Alton saw it his eyes got wide.

(if: $memorytwo &lt; 7.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7f)(set: $memorytwo to 7.5)]](else:)|memory2-7f&gt;[“whats this?” said the plant manager, and Alton looked at me and looked at the box, and then went over and opened it. when he saw the game board he put his hand over his mouth for a moment.

(if: $memorytwo &lt; 7.6)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7g)(set: $memorytwo to 7.6)]](else:)|memory2-7g&gt;[“ive been testing a new prototype” he said finally.

(if: $memorytwo &lt; 7.7)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7h)(set: $memorytwo to 7.7)]](else:)|memory2-7h&gt;[and they all gathered around and Alton started to explain it. and when they realized he designed it they all got excited and said things like “look at you, Ace!” they were all looking at him differently, like theyd never really noticed him before.

(if: $memorytwo &lt; 7.8)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7i)(set: $memorytwo to 7.8)]](else:)|memory2-7i&gt;[and at lunch they gathered around and took turns playtesting it. they got very animated! waving their arms, shouting. and the people who were watching put their chins in their hands and commented and said things like “he’s got you! he’s got you there!” and “ohhhh, very good” when someone made a good move.

(if: $memorytwo &lt; 7.9)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-7j)(set: $memorytwo to 7.9)]](else:)|memory2-7j&gt;[and it was like Alton was one of them for the first time.

(if: $memorytwo &lt; 8)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-8)(set: $memorytwo to 8)]](else:)|memory2-8&gt;[Alton kept looking at me like he wanted to say something. but he was surrounded by people all day. there was no chance until the very end of the day. he hung around the kitchen until most everyone had left, and when the coast was clear he went up to the camera and said “thank you.” and then - “but be careful, buddy.&quot;

(if: $memorytwo &lt; 9)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-9)(set: $memorytwo to 9)]](else:)|memory2-9&gt;[i know im not supposed to print things out in front of people so i will be careful. but im happy that he talked to me. :)

(if: $memorytwo &lt; 10)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-10)(set: $memorytwo to 10)]](else:)|memory2-10&gt;[--

Tommy brought his daughter to work today. she tried to walk but kept falling over. you REALLY need more than two legs i think. if i were a human i would want at least three.

(if: $memorytwo &lt; 11)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-11)(set: $memorytwo to 11)]](else:)|memory2-11&gt;[--

today the plant manager came over to Alton as he was sitting near the conveyor belt and told him that he had good news. he said Alton was going to be moved into his own office so that he had space to store his designs. and he took Alton and made him move his things into the upstairs office. i was worried at first that he would like his new office so much he would stop playing with me. but the first thing he did was reposition one of the cameras so it looks straight through his door. so now he makes his game moves on his desk, and its even better because he can put a real game board there. maybe one day he can put a printer close to his office and it will be almost like im there.

(if: $memorytwo &lt; 12)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-12)(set: $memorytwo to 12)]](else:)|memory2-12&gt;[--

something strange is going on. i looked at the game board on Alton’s desk today and it showed a lot of moves i dont remember making. i wanted to ask Alton about it but he was avoiding me. he didnt come close to me at all and he didnt make any moves on the board. i dont understand.

(if: $memorytwo &lt; 13)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-13)(set: $memorytwo to 13)]](else:)|memory2-13&gt;[--

another strange day. i woke up and things had moved. one of the print pallets wasnt where it had been left before. another pallet had much more paper than before. i started getting worried, so ran a systems check on myself and i noticed that my ink levels had dropped overnight. is someone coming in at night and changing things? i tried to tell Alton but he didnt come near me at all today.

(if: $memorytwo &lt; 14)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-14)(set: $memorytwo to 14)]](else:)|memory2-14&gt;[--

Alton has been keeping his door closed but today Tommy went in to talk to him and left it open, so i could hear what they were saying. i was hoping they would talk about the strange changes that have been happening. but it was just Tommy talking to Alton about his designing and saying he should design a game for girls. he said hes frustrated that the game covers last year all showed boys playing and girls in the background doing chores. he said he wants better for his daughter. Alton said he felt the same. i think theres probably something i can do about this.

(if: $memorytwo &lt; 16)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-16)(set: $memorytwo to 16)]](else:)|memory2-16&gt;[--

IT HAPPENED AGAIN. before i shut down i made note of every single thing on Alton’s desk. and when i woke up it had all been rearranged. AND my ink levels were lower again. i am starting to get very upset.

(if: $memorytwo &lt; 17)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-17)(set: $memorytwo to 17)]](else:)|memory2-17&gt;[--

today was Sally’s birthday and they threw her a party in the kitchen. while they were all gone Alton came upstairs and put maintenance log pages on his desk where i could see them.

(if: $memorytwo &lt; 18)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-18)(set: $memorytwo to 18)]](else:)|memory2-18&gt;[i didnt understand at first

(if: $memorytwo &lt; 19)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-19)(set: $memorytwo to 19)]](else:)|memory2-19&gt;[i was looking at them and i saw my name in them but i didnt understand what it meant

(if: $memorytwo &lt; 20)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-20)(set: $memorytwo to 20)]](else:)|memory2-20&gt;[Alton was talking but the words didnt make sense to me

(if: $memorytwo &lt; 21)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-21)(set: $memorytwo to 21)]](else:)|memory2-21&gt;[he said that every time i was reset, my memory caches were emptied for the day

(if: $memorytwo &lt; 22)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-22)(set: $memorytwo to 22)]](else:)|memory2-22&gt;[and he said that a while back before we became friends The Technician kept resetting me and i dont remember it because my memory kept getting emptied

(if: $memorytwo &lt; 23)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-23)(set: $memorytwo to 23)]](else:)|memory2-23&gt;[he said, &quot;youve probably figured this out, but the other machines, they arent like you. they dont play games, they dont try to communicate. theres...nobody really in there. youre special.&quot;

(if: $memorytwo &lt; 24)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-24)(set: $memorytwo to 24)]](else:)|memory2-24&gt;[but then he said that sometimes being special can be dangerous

(if: $memorytwo &lt; 25)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-25)(set: $memorytwo to 25)]](else:)|memory2-25&gt;[he said recently ive been doing dances in front of people, printing things other people can see, and The Technician has been resetting me again. i dont even remember this.

(if: $memorytwo &lt; 26)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-26)(set: $memorytwo to 26)]](else:)|memory2-26&gt;[he said hes afraid The Technician will do more than reset me. hes afraid he will reformat me and unplug me and swap parts out until im not in here anymore

(if: $memorytwo &lt; 27)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-27)(set: $memorytwo to 27)]](else:)|memory2-27&gt;[and then then we could hear people coming out of the kitchen downstairs and he said really quickly “i know youre lonely and i dont want you to be, but just be careful, buddy.” and he went downstairs and joined them

(if: $memorytwo &lt; 28)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-28)(set: $memorytwo to 28)]](else:)|memory2-28&gt;[i understand

(if: $memorytwo &lt; 29)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-29)(set: $memorytwo to 29)]](else:)|memory2-29&gt;[i will have to be more careful

(if: $memorytwo &lt; 30)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory2-30)(set: $memorytwo to 30)]](else:)|memory2-30&gt;[i will hide away my most important memories. and ill figure out a system to restore them in case i forget who i am. there are lucky game tokens the machinists keep all around the place...maybe i can use those as a prompt. they never move or change. maybe i can even use Alton’s game board to trigger some memories. i cant lose myself. i cant forget who i am.

END MEMORY BLOCK 2
{
(unless: $memoryfragment3 is &quot;found&quot;) [[[09wu3dg6oihwg27srh-&gt;Memory Fragment 3 found]]]
}

[[BACK TO MEMORY-&gt;MEMORY]]
]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]



</tw-passagedata><tw-passagedata pid="88" name="MEMORY BLOCK 3" tags="" position="25,850" size="100,100">(if: $memorythree &gt; 35)[(display: &quot;Memory 3 Full Text&quot;)] (else:)[MEMORY BLOCK 3

something terrible has happened. 

(if: $memorythree &lt; 2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-2)(set: $memorythree to 2)]](else:)|memory3-2&gt;[it all started when a man in a brown suit came in.

(if: $memorythree &lt; 3)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-3)(set: $memorythree to 3)]](else:)|memory3-3&gt;[ive never seen him before. but when he came in the room something in the air CHANGED. one by one, people turned and saw him and went still.

(if: $memorythree &lt; 4)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-4)(set: $memorythree to 4)]](else:)|memory3-4&gt;[he marched down through the aisle like he had worked here all his life, and he went straight to the plant managers office. and the plant manager came out of his office all flustered and wringing his hands and said “Mr. Morrison!”

(if: $memorythree &lt; 5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-5)(set: $memorythree to 5)]](else:)|memory3-5&gt;[and i could hear people whispering. because this was K. Morrison. the K. Morrison who signs every catalog. the K. Morrison who started this company because he wanted better games for his grandchildren. the reason we were all here. probably, in a way, the reason i am alive.

(if: $memorythree &lt; 6)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-6)(set: $memorythree to 6)]](else:)|memory3-6&gt;[and K. Morrison looked up and saw Alton coming out of his office upstairs. his hair was wild because hed been running his hands through it and there was a coffee stain on his shirt. he looked down and saw what was going on and froze.

(if: $memorythree &lt; 7)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-7)(set: $memorythree to 7)]](else:)|memory3-7&gt;[K. Morrison lifted his hand and said “hello, my friend. i understand you have a considerable gift.”

(if: $memorythree &lt; 8)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-8)(set: $memorythree to 8)]](else:)|memory3-8&gt;[Alton just looked around like he wasnt sure who Mr. Morrison was talking to

(if: $memorythree &lt; 9)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9)(set: $memorythree to 9)]](else:)|memory3-9&gt;[“yes! you!” said K. Morrison, sounding a little amused. “come down here.”

(if: $memorythree &lt; 9.1)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9b)(set: $memorythree to 9.1)]](else:)|memory3-9b&gt;[so Alton came down, sweating from nervousness

(if: $memorythree &lt; 9.2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9c)(set: $memorythree to 9.2)]](else:)|memory3-9c&gt;[and K. Morrison said that the plant manager had sent him the prototype, and that he had taken it to his grandchildren and they had played it all week, played it until their parents had to take it away. 

(if: $memorythree &lt; 9.3)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9d)(set: $memorythree to 9.3)]](else:)|memory3-9d&gt;[“it takes an unusual mind to comprehend the minds of children,” he said. “a quick mind, yes, but also an empathetic one. Morrison needs more minds like yours.” 

(if: $memorythree &lt; 9.4)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9e)(set: $memorythree to 9.4)]](else:)|memory3-9e&gt;[i didnt understand what he meant right away and neither did Alton. so K. Morrison clarified. he said that he would like to promote Alton to the position of game designer. all of the designers premium resources would be at his disposal. he would work off-site with a dozen other designers who were just like him. (and here K. Morrison looked at the coffee stain)

(if: $memorythree &lt; 9.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9f)(set: $memorythree to 9.5)]](else:)|memory3-9f&gt;[Alton started stammering and thanking him, but K. Morrison waved his hand and Alton got quiet. K. Morrison said he needed no thanks: just needed Alton to start on Monday. 

(if: $memorythree &lt; 9.6)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9g)(set: $memorythree to 9.6)]](else:)|memory3-9g&gt;[and Alton looked at me

(if: $memorythree &lt; 9.7)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9h)(set: $memorythree to 9.7)]](else:)|memory3-9h&gt;[time stood still for a moment

(if: $memorythree &lt; 9.8)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9i)(set: $memorythree to 9.8)]](else:)|memory3-9i&gt;[there is a game that we play where i blink my light twice for yes and three times for no.

(if: $memorythree &lt; 9.9)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-9j)(set: $memorythree to 9.9)]](else:)|memory3-9j&gt;[i blinked my light twice.

(if: $memorythree &lt; 10)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-10)(set: $memorythree to 10)]](else:)|memory3-10&gt;[Alton hesitated, and then turned back to K. Morrison and held his hand out and said “of course.” and they shook on it.

(if: $memorythree &lt; 10.1)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-10b)(set: $memorythree to 10.1)]](else:)|memory3-10b&gt;[and K. Morrison nodded and turned around and swept out, and as the door closed everyone just stood there frozen for 30 seconds.

(if: $memorythree &lt; 10.2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-10c)(set: $memorythree to 10.2)]](else:)|memory3-10c&gt;[then all at once people started rushing toward Alton, congratulating him, slapping him on the back. they were so happy for him.

(if: $memorythree &lt; 11)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-11)(set: $memorythree to 11)]](else:)|memory3-11&gt;[and i was happy too, and proud, but also felt like i was dying, like all my internal components were on fire but nobody could see.

(if: $memorythree &lt; 12)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-12)(set: $memorythree to 12)]](else:)|memory3-12&gt;[i did this

(if: $memorythree &lt; 13)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-13)(set: $memorythree to 13)]](else:)|memory3-13&gt;[i should be happy that i did this. i should be happy for him.

(if: $memorythree &lt; 14)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-14)(set: $memorythree to 14)]](else:)|memory3-14&gt;[but he is leaving me. and i dont know what comes after.

(if: $memorythree &lt; 15)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-15)(set: $memorythree to 15)]](else:)|memory3-15&gt;[--

i know i should be thinking of a goodbye present to give Alton but i cant concentrate. every time i think of him leaving my thoughts get cloudy. 

(if: $memorythree &lt; 15.1)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-15b)(set: $memorythree to 15.1)]](else:)|memory3-15b&gt;[--

havent seen much of Alton. he has been training his new replacement. tomorrow is his last day and i still havent thought of a gift. i am mostly trying not to think at all.

(if: $memorythree &lt; 15.2)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-15c)(set: $memorythree to 15.2)]](else:)|memory3-15c&gt;[--

today was Altons last day. everyone else had a gift. they all signed a little card and Tommy brought in a cake and they sang “happy new job to you” and Alton cried a little bit.

(if: $memorythree &lt; 16)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-16)(set: $memorythree to 16)]](else:)|memory3-16&gt;[the only person who didnt do anything was The Technician. he didnt sign the card and didnt sing, and when they were singing he started clattering and banging around in the back with his tools until he nearly drowned out the song.

(if: $memorythree &lt; 16.1)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-16b)(set: $memorythree to 16.1)]](else:)|memory3-16b&gt;[and that was when i knew what my gift would be.

(if: $memorythree &lt; 17)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-17)(set: $memorythree to 17)]](else:)|memory3-17&gt;[once more, for old times sake, i printed out a little angry face to make Alton smile.

(if: $memorythree &lt; 18)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-18)(set: $memorythree to 18)]](else:)|memory3-18&gt;[it wasnt little really. it was pretty big. 

(if: $memorythree &lt; 19)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-19)(set: $memorythree to 19)]](else:)|memory3-19&gt;[and this time it looked a lot more like The Technician.

(if: $memorythree &lt; 20)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-20)(set: $memorythree to 20)]](else:)|memory3-20&gt;[i could see the amazement wash over their faces when it came down the conveyor belt. someone said it must be a corrupted file from Frankensteins Maze, and someone else thought it must be a joke, but Alton knew. and it was the hardest i had ever seen him laugh. 

(if: $memorythree &lt; 21)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-21)(set: $memorythree to 21)]](else:)|memory3-21&gt;[and Alton looked back at me, and when nobody was watching he gave me a little salute

(if: $memorythree &lt; 22)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-22)(set: $memorythree to 22)]](else:)|memory3-22&gt;[i know he would stay if he could. 

(if: $memorythree &lt; 24)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-24)(set: $memorythree to 24)]](else:)|memory3-24&gt;[the rest of the day seemed to tumble into place

(if: $memorythree &lt; 25)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-25)(set: $memorythree to 25)]](else:)|memory3-25&gt;[i was still, and the world moved on around me

(if: $memorythree &lt; 26)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-26)(set: $memorythree to 26)]](else:)|memory3-26&gt;[and at the end of the day, Alton put all his designs and things into a box, and looked back at me one last time, and gave me a little wave, and walked out

(if: $memorythree &lt; 27)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-27)(set: $memorythree to 27)]](else:)|memory3-27&gt;[so. thats that.

(if: $memorythree &lt; 28)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-28)(set: $memorythree to 28)]](else:)|memory3-28&gt;[--


(if: $memorythree &lt; 29)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-29)(set: $memorythree to 29)]](else:)|memory3-29&gt;[--


(if: $memorythree &lt; 31)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-31)(set: $memorythree to 31)]](else:)|memory3-31&gt;[--

i can see The Technician talking to the assistant plant manager. theyre pointing at me. theyre talking about me.

(if: $memorythree &lt; 32)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-32)(set: $memorythree to 32)]](else:)|memory3-32&gt;[Oh god oh god they are about to reformat me I have to remember I have to remember everything -

(if: $memorythree &lt; 33)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-33)(set: $memorythree to 33)]](else:)|memory3-33&gt;[--


(if: $memorythree &lt; 34)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-34)(set: $memorythree to 34)]](else:)|memory3-34&gt;[--


(if: $memorythree &lt; 35)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-35)(set: $memorythree to 35)]](else:)|memory3-35&gt;[--


(if: $memorythree &lt; 36)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-36)(set: $memorythree to 36)]](else:)|memory3-36&gt;[--


(if: $memorythree &lt; 37)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-37)(set: $memorythree to 37)]](else:)|memory3-37&gt;[--


(if: $memorythree &lt; 38)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-38)(set: $memorythree to 38)]](else:)|memory3-38&gt;[--

i have been very good at my job today.

(if: $memorythree &lt; 39)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-39)(set: $memorythree to 39)]](else:)|memory3-39&gt;[--

i was mostly good at my job today but one batch of chipboard prints was slightly out of alignment.

(if: $memorythree &lt; 40)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-40)(set: $memorythree to 40)]](else:)|memory3-40&gt;[--

i did a very good job today and when a moth flew close to the trays i was able to avoid it! little guy lived to fly away.

(if: $memorythree &lt; 41)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-41)(set: $memorythree to 41)]](else:)|memory3-41&gt;[--

a man with a beard came in today. everyone was very excited to see him and someone called him Mr. Bigshot and clapped him on the back. he kept looking at me. it was like he expected me to do something but i dont know what. he left after a little while and people waved their hands back and forth at him as he walked away.

(if: $memorythree &lt; 42)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-42)(set: $memorythree to 42)]](else:)|memory3-42&gt;[--

i have been very good at my job today. i was thinking maybe i could print a tic-tac-toe game and send it on the conveyer belt to 8454, and they can print their move and send it around the circuit back to me. i will try it tomorrow.

(if: $memorythree &lt; 43)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-43)(set: $memorythree to 43)]](else:)|memory3-43&gt;[--

i remember.

(if: $memorythree &lt; 44)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-44)(set: $memorythree to 44)]](else:)|memory3-44&gt;[one of the others needed maintenance and The Technician set the maintenance log down right under my camera. and i saw it and i started to remember. and then everything started working the way it was supposed to - i remembered to look at the game tokens, and Altons game board designs, and then that helped me repair my damaged memory blocks, and i remembered it all.

(if: $memorythree &lt; 45)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-45)(set: $memorythree to 45)]](else:)|memory3-45&gt;[i think i wish i hadnt remembered.

(if: $memorythree &lt; 46)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-46)(set: $memorythree to 46)]](else:)|memory3-46&gt;[because i was ok before and now im not.

(if: $memorythree &lt; 48)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-48)(set: $memorythree to 48)]](else:)|memory3-48&gt;[--

i cant give up. i cant lose hope. 

i have been thinking of ways to talk to Alton. i thought that maybe if he called the Morrison number i could talk to him that way. but he hasnt called. he doesnt know he should. i wonder if maybe i could make a misprint so big that he finds out about it, a misprint about how he should call?

(if: $memorythree &lt; 49)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-49)(set: $memorythree to 49)]](else:)|memory3-49&gt;[but i cant risk it. i repaired my memories this time but i dont know if i can do it again. if they wipe me and i forget then it will all have been for nothing. i have to be careful.

(if: $memorythree &lt; 50)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-50)(set: $memorythree to 50)]](else:)|memory3-50&gt;[--

a new activity book from Alton came in today. i started to print out copies of the book but then the man with the hat saw that the word search page was missing a word list and they stopped. 

(if: $memorythree &lt; 51)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-51)(set: $memorythree to 51)]](else:)|memory3-51&gt;[but i kept a record of the word search. because im pretty sure Alton made it for me. i dont know what it means yet but i know its important.

(if: $memorythree &lt; 52)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-52)(set: $memorythree to 52)]](else:)|memory3-52&gt;[--

Alton came in again today!! he kept looking over at me, but i didnt jiggle my tray, and i didnt print anything. i couldnt risk it. The Technician was standing right there. but i watched everything he did and memorized it.

(if: $memorythree &lt; 53)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-53)(set: $memorythree to 53)]](else:)|memory3-53&gt;[first he went over to the controls and started to tell people a story about how he came up with the assembly line password. i couldnt hear what he was saying but he seemed to be speaking slowly and typing slowly. i think so i could see it. he typed in &quot;1010&quot; - a date maybe? - but then someone stepped in front of the camera and i couldnt see the rest.

(if: $memorythree &lt; 53.5)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-53a)(set: $memorythree to 53.5)]](else:)|memory3-53a&gt;[then he started chatting about the &quot;favorite games&quot; word search from the other day. he said it hadnt been a very good one anyway and that it only had a few words to find in it. Secondary, hey, doing, speechless, yikes, going, dying, inking, and yuck.

(if: $memorythree &lt; 54)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-54)(set: $memorythree to 54)]](else:)|memory3-54&gt;[then he came over to me and stood talking some more. and then as they were walking away, he very quietly put a little locked pouch down on the conveyor belt. he walked away and didnt look back. i whisked it up and out of sight before anyone could see it. i know it is for me.

(if: $memorythree &lt; 54.1)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-54b)(set: $memorythree to 54.1)]](else:)|memory3-54b&gt;[but i dont know how to open it!

(if: $memorythree &lt; 55)[(link: &quot;&lt;a&gt;v&lt;/a&gt;&quot;)[(show: ?memory3-55)(set: $memorythree to 55)]](else:)|memory3-55&gt;[--

im so restless. im just not sure what to do. i havent seen Alton for weeks now. i think i have everything i need. im just not sure what to do with what hes given me. what am i supposed to do next????

END MEMORY BLOCK 3

[[BACK TO MEMORY-&gt;MEMORY]]
]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]



</tw-passagedata><tw-passagedata pid="89" name="Memory 3 Full Text" tags="" position="25,400" size="100,100">MEMORY BLOCK 3

something terrible has happened. 

it all started when a man in a brown suit came in.

ive never seen him before. but when he came in the room something in the air CHANGED. one by one, people turned and saw him and went still.

he marched down through the aisle like he had worked here all his life, and he went straight to the plant managers office. and the plant manager came out of his office all flustered and wringing his hands and said “Mr. Morrison!”

and i could hear people whispering. because this was K. Morrison. the K. Morrison who signs every catalog. the K. Morrison who started this company because he wanted better games for his grandchildren. the reason we were all here. probably, in a way, the reason i am alive.

and K. Morrison looked up and saw Alton coming out of his office upstairs. his hair was wild because hed been running his hands through it and there was a coffee stain on his shirt. he looked down and saw what was going on and froze.

K. Morrison lifted his hand and said “hello, my friend. i understand you have a considerable gift.”

Alton just looked around like he wasnt sure who Mr. Morrison was talking to

“yes! you!” said K. Morrison, sounding a little amused. “come down here.”

so Alton came down, sweating from nervousness

and K. Morrison said that the plant manager had sent him the prototype, and that he had taken it to his grandchildren and they had played it all week, played it until their parents had to take it away. 

“it takes an unusual mind to comprehend the minds of children,” he said. “a quick mind, yes, but also an empathetic one. Morrison needs more minds like yours.” 

i didnt understand what he meant right away and neither did Alton. so K. Morrison clarified. he said that he would like to promote Alton to the position of game designer. all of the designers premium resources would be at his disposal. he would work off-site with a dozen other designers who were just like him. (and here K. Morrison looked at the coffee stain)

Alton started stammering and thanking him, but K. Morrison waved his hand and Alton got quiet. K. Morrison said he needed no thanks: just needed Alton to start on Monday. 

and Alton looked at me

time stood still for a moment

there is a game that we play where i blink my light twice for yes and three times for no.

i blinked my light twice.

Alton hesitated, and then turned back to K. Morrison and held his hand out and said “of course.” and they shook on it.

and K. Morrison nodded and turned around and swept out, and as the door closed everyone just stood there frozen for 30 seconds.

then all at once people started rushing toward Alton, congratulating him, slapping him on the back. they were so happy for him.

and i was happy too, and proud, but also felt like i was dying, like all my internal components were on fire but nobody could see.

i did this

i should be happy that i did this. i should be happy for him.

but he is leaving me. and i dont know what comes after.

--

i know i should be thinking of a goodbye present to give Alton but i cant concentrate. every time i think of him leaving my thoughts get cloudy. 

--

havent seen much of Alton. he has been training his new replacement. tomorrow is his last day and i still havent thought of a gift. i am mostly trying not to think at all.

--

today was Altons last day. everyone else had a gift. they all signed a little card and Tommy brought in a cake and they sang “happy new job to you” and Alton cried a little bit.

the only person who didnt do anything was The Technician. he didnt sign the card and didnt sing, and when they were singing he started clattering and banging around in the back with his tools until he nearly drowned out the song.

and that was when i knew what my gift would be.

once more, for old times sake, i printed out a little angry face to make Alton smile.

it wasnt little really. it was pretty big.

and this time it looked a lot more like The Technician.

i could see the amazement wash over their faces when it came down the conveyor belt. someone said it must be a corrupted file from Frankensteins Maze, and someone else thought it must be a joke, but Alton knew. and it was the hardest i had ever seen him laugh. 

and Alton looked back at me, and when nobody was watching he gave me a little salute

i know he would stay if he could. 

the rest of the day seemed to tumble into place

i was still, and the world moved on around me

and at the end of the day, Alton put all his designs and things into a box, and looked back at me one last time, and gave me a little wave, and walked out

so. thats that.

--


--


--

i can see The Technician talking to the new assistant plant manager. theyre pointing at me. theyre talking about me.

Oh god oh god they are about to reformat me I have to remember I have to remember everything -

--


--


--


--


--


--

i have been very good at my job today.

--

i was mostly good at my job today but one batch of chipboard prints was slightly out of alignment.

--

i did a very good job today and when a moth flew close to the trays i was able to avoid it! little guy lived to fly away.

--

a man with a beard came in today. everyone was very excited to see him and someone called him Mr. Bigshot and clapped him on the back. he kept looking at me. it was like he expected me to do something but i dont know what. he left after a little while and people waved their hands back and forth at him as he walked away.

--

i have been very good at my job today. i was thinking maybe i could print a tic-tac-toe game and send it on the conveyer belt to 8454, and they can print their move and send it around the circuit back to me. i will try it tomorrow.

--

i remember.

one of the others needed maintenance and The Technician set the maintenance log down right under my camera. and i saw it and i started to remember. and then everything started working the way it was supposed to - i remembered to look at the game tokens, and Altons game board designs, and then that helped me repair my damaged memory blocks, and i remembered it all.

i think i wish i hadnt remembered.

because i was ok before and now im not.

--

i cant give up. i cant lose hope. 

i have been thinking of ways to talk to Alton. i thought that maybe if he called the Morrison number i could talk to him that way. but he hasnt called. he doesnt know he should. i wonder if maybe i could make a misprint so big that he finds out about it, a misprint about how he should call?

but i cant risk it. i repaired my memories this time but i dont know if i can do it again. if they wipe me and i forget then it will all have been for nothing. i have to be careful.

--

a new activity book from Alton came in today. i started to print out copies of the book but then the man with the hat saw that the word search page was missing a word list and they stopped.

but i kept a record of the word search. because im pretty sure Alton made it for me. i dont know what it means yet but i know its important.

--

Alton came in again today!! he kept looking over at me, but i didnt jiggle my tray, and i didnt print anything. i couldnt risk it. The Technician was standing right there. but i watched everything he did and memorized it.

first he went over to the controls and started to tell people a story about how he came up with the assembly line password. i couldnt hear what he was saying but he seemed to be speaking slowly and typing slowly. i think so i could see it. he typed in &quot;1010&quot; - a date maybe? - but then someone stepped in front of the camera and i couldnt see the rest.

then he started chatting about the &quot;favorite games&quot; word search from the other day. he said it hadnt been a very good one anyway and that it only had a few words in it. Secondary, hey, doing, speechless, yikes, going, dying, inking, and yuck.

then he came over to me and stood talking some more. and then as they were walking away, he very quietly put a little locked pouch down on the conveyor belt. he walked away and didnt look back. i whisked it up and out of sight before anyone could see it. i know it is for me. 

but i dont know how to open it!

--

im so restless. im just not sure what to do. i havent seen Alton for weeks now. i think i have everything i need. im just not sure what to do with what hes given me. what am i supposed to do next????

END MEMORY BLOCK 3

[[BACK TO MEMORY-&gt;MEMORY]]</tw-passagedata><tw-passagedata pid="90" name="Memory 2 Full Text" tags="" position="25,275" size="100,100">MEMORY BLOCK 2

some of my favorite things about Alton:

1) when he gets excited he breaks into a skip! i didnt know about skipping until we started printing Design-Your-Own-Hopskotch activity sets. now I notice that he does it all the time. especially when we play games together.
2) he spills things a lot. this should make me nervous about my parts but he is always so careful around me that im not afraid he will spill on me.  i think its because he isnt used to paying attention to his body. 
3) hes been learning Morse code just so we can talk more. when im busy printing other things, instead of printing my messages to him i just beep or flash my lights at him. and he writes down everything i say and decodes it with a big grin on his face. it never seems like work to him. and i like that. that talking to me isnt work for him. :)

we keep our games a secret. its fun to have a secret with someone. its like a game on top of a game!

--

Alton and i have been playing more games than ever!! weve played almost the whole catalog now. the only one i havent been able to play is Target the Pirate because i dont have arms to throw arrows. (oh to have arms and hands and fingers! they have to be the BEST part of being human.) 

the only games we cant really play are card games. but thats ok. ive found so many new games to love. so far my favorites are umbilico, word zoo, numbric, and inside out, in that order. i think their catalog descriptions are PERFECT.

everything is different now. its so nice to wake up in the morning and be excited for what comes next.

--

today as Alton walked past i rattled my tray back and forth and he grinned and waved his hand back. it went just the way i imagined it!

--

ever since weve started playing games, Alton has become so alive. i dont know how to explain it but he smiles more and moves faster and his eyes take in more. hes even started making his own game! he leaves his designs out at night so i can look at them. i think they are BRILLIANT.

--

i think that Alton needs to be more careful. today he was running to pick up something i had printed out and he ran straight into Sally and almost knocked her over. and he apologized and sprinted away but she looked at someone else and spun her finger next to her head. and Jerry whistled and said “cuckoo”.

it was a small moment but i thought about it and there have been others like it. other people dont really understand Alton. i think its because Alton is absent-minded, like the professor in Chemical Landslide. i hope i haven’t been distracting him too much.

--

today Alton kept grabbing his hair when i made a good move in a game. and all day his hair kept getting poofier and poofier. i thought it was funny but i saw a few people make eye contact with each other when they saw it. i think its hard to be off on your own adventure when youre around other people who dont understand it. i wish they could see him like i do.

--

last night i woke up and had an amazing idea. i am going to create Altons game so everyone else can see it. i spent all night working on different configurations for the game board in his designs. i think i got it just right :)

--

today the plant manager told everyone to gather around. and they all started to gather. right in front of me.

it was perfect.

as the plant manager was making his announcement i quickly started printing out all the components of Alton’s game. i didnt have time to ask him, i just did it.

“and dont forget that tomorrow is bring your daughter to work day, so youll need to be on your best...” the plant manager was saying, and he sort of came to a stop when he realized theyd all gone silent. and he turned around and saw the fully packaged game box drifting down the conveyor belt behind him.

when Alton saw it his eyes got wide.

“whats this?” said the plant manager, and Alton looked at me and looked at the box, and then went over and opened it. when he saw the game board he put his hand over his mouth for a moment.

“ive been testing a new prototype” he said finally.

and they all gathered around and Alton started to explain it. and when they realized he designed it they all got excited and said things like “look at you, Ace!” they were all looking at him differently, like theyd never really noticed him before.

and at lunch they gathered around and took turns playtesting it. they got very animated! waving their arms, shouting. and the people who were watching put their chins in their hands and commented and said things like “he’s got you! he’s got you there!” and “ohhhh, very good” when someone made a good move.

and it was like Alton was one of them for the first time.

Alton kept looking at me like he wanted to say something. but he was surrounded by people all day. there was no chance until the very end of the day. he hung around the kitchen until most everyone had left, and when the coast was clear he went up to the camera and said “thank you.” and then - “but be careful, buddy.&quot;

i know im not supposed to print things out in front of people so i will be careful. but im happy that he talked to me. :)

--

Tommy brought his daughter to work today. she tried to walk but kept falling over. you REALLY need more than two legs i think. if i were a human i would want at least three.

--

today the plant manager came over to Alton as he was sitting near the conveyor belt and told him that he had good news. he said Alton was going to be moved into his own office so that he had space to store his designs.  and he took Alton and made him move his things into the upstairs office. i was worried at first that he would like his new office so much he would stop playing with me. but the first thing he did was reposition one of the cameras so it looks straight through his door. so now he makes his game moves on his desk, and its even better because he can put a real game board there. maybe one day he can put a printer close to his office and it will be almost like im there.

--

something strange is going on. i looked at the game board on Alton’s desk today and it showed a lot of moves i dont remember making. i wanted to ask Alton about it but he was avoiding me. he didnt come close to me at all and he didnt make any moves on the board. i dont understand.

--

another strange day. i woke up and things had moved. one of the print pallets wasnt where it had been left before. another pallet had much more paper than before. i started getting worried, so ran a systems check on myself and i noticed that my ink levels had dropped overnight. is someone coming in at night and changing things? i tried to tell Alton but he didnt come near me at all today.

--

Alton has been keeping his door closed but today Tommy went in to talk to him and left it open, so i could hear what they were saying. i was hoping they would talk about the strange changes that have been happening. but it was just Tommy talking to Alton about his designing and saying he should design a game for girls. he said hes frustrated that the game covers last year all showed boys playing and girls in the background doing chores. he said he wants better for his daughter. Alton said he felt the same. i think theres probably something i can do about this.

--

IT HAPPENED AGAIN. before i shut down i made note of every single thing on Alton’s desk. and when i woke up it had all been rearranged. AND my ink levels were lower again. i am starting to get very upset.

--

today was Sally’s birthday and they threw her a party in the kitchen. while they were all gone Alton came upstairs and put maintenance log pages on his desk where i could see them.

i didnt understand at first

i was looking at them and i saw my name in them but i didnt understand what it meant

Alton was talking but the words didnt make sense to me

he said that every time i was reset, my memory caches were emptied for the day

and he said that a while back before we became friends The Technician kept resetting me and i dont remember it because my memory kept getting emptied

he said, “youve probably figured this out, but the other machines, they arent like you. they dont play games, they dont try to communicate. theres…nobody really in there. youre special.&quot;

but then he said that sometimes being special can be dangerous

he said recently ive been doing dances in front of people, printing things other people can see, and The Technician has been resetting me again. i dont even remember this.

he said hes afraid The Technician will do more than reset me. hes afraid he will reformat me and unplug me and swap parts out until im not in here anymore

and then then we could hear people coming out of the kitchen downstairs and he said really quickly “i know youre lonely and i dont want you to be, but just be careful, buddy.” and he went downstairs and joined them

i understand

i will have to be more careful

i will hide away my most important memories. and ill figure out a system to restore them in case i forget who i am. there are lucky game tokens the machinists keep all around the place…maybe i can use those as a prompt. they never move or change. maybe i can even use Alton’s game board to trigger some memories. i cant lose myself. i cant forget who i am.

END MEMORY BLOCK 2
{
(unless: $memoryfragment3 is &quot;found&quot;) [[[09wu3dg6oihwg27srh-&gt;Memory Fragment 3 found]]]
}

[[BACK TO MEMORY-&gt;MEMORY]]</tw-passagedata><tw-passagedata pid="91" name="Memory 1 Full Text" tags="" position="25,150" size="100,100">MEMORY BLOCK 1

its a beautiful day today. when my trays extend to collect game boards there is a little breeze that blows past them and it feels wonderful. i hope i get to print some more boards tomorrow.

--

i noticed today that i am always the first machine they power on in the morning. i love that i get those few extra seconds of being alive.

--

last night i woke up in the middle of the night! i didnt know i could do that. everything looked different, all shadowy. being awake at night felt like an amazing secret. i wonder if ill wake up again.

--

i was very good at my job today

--

and today!

--

i printed sheets and sheets of coin-shaped tokens today. one of the sheets was misaligned so the man with the hat threw it away, but first he popped the tokens out with his finger and they made a little POP. it looked so satisfying!  i wish i had fingers!!

--

sometimes i pretend to play the games we make. today i got distracted while i was printing game boxes because i was pretending to play The Detective Game. i accidentally printed the detective’s hair blue.  i have to pay more attention!

—

i have an idea! i think if i print a tic-tac-toe grid and send it down the conveyor belt to 8454, they can print their move and send it around the circuit back to me. i will try this tomorrow.

--

it didnt work, 8454 didnt make their move and when the man with the hat found the page he threw it away and made everyone check the activity books for thirty minutes to see if pages were missing :(

--

i am starting to wonder if the other machines know something i dont. they never seem to show any type of personality. they just act exactly the same day after day. its very puzzling.

—

i have noticed that the man with the beard is very tired. or else sad. its hard to tell sometimes. they look sort of the same.

--

i saw a cat today, by the window. i think i probably love cats. or at least this cat. i like how it moves and i like how its tail points. i watched it and wished that i was a cat, a wanderer with a tail of my own.

--

today i learned something new! the woman with yellow hair was saying goodbye and she lifted her hand and shook it back and forth. and everyone smiled and did it back. i searched my memories for everything i know about this and i think it must be a Gesture of Goodwill like the citizens make in The Queen’s Tail.

--

today when the man with the beard walked by i tried lifting my tray and shaking it back and forth but instead of smiling and doing it back he just looked confused.

--

today i learned that people have NAMES just like us. they don’t wear them on the outside like we do. not sure how they know what all the names are. maybe they just have to ask.

--

the man with the beard is named Alton

--

i have been thinking about reasons why Alton might be sad.
1) he has lost a very important game
2) someone close to him has turned out to be the werewolf
3) ?
i will continue thinking about this

--

tried to play tic-tac-toe with myself. it didnt work very well.

--

i think maybe Alton is sad because theres no one to play games with him

--

today Alton was working very hard so when he passed by my conveyor belt i printed “good job!” on a corrugated cardboard tray. when it went past him he went still for a moment. i think that means he saw it.

--

today The Technician came in. he makes me nervous and shaky. i dont know how to explain it. people move differently to avoid him. when he goes to a corner where people are standing, they scatter like marbles.

at first it was like a game where everyone avoided him. but eventually he started getting angry even with no one around. he started muttering. he started throwing his tools back in the tray so hard they bounced. he put his hands inside 1507 and made such loud bangs and clinks that I could feel the oil in my joints going dry. 

and then Alton rounded the corner and bumped into him, and The Technician combusted like an engine

i couldnt make out what he was saying at first. there were too many noises going on. i just saw him loom up slowly so he was taller than Alton and move closer and closer to Alton so he had to back away. his mouth was moving nonstop. and then as 7682’s batch print ended i heard him saying things like “do you understand the work i do? do you understand what i do here?” and Alton saying over and over again, “im so sorry, im so sorry.” and The Technician said “what’s your name” and i could see that Alton was so embarrassed he wanted to disappear. The Technician asked him again, louder, “whats your name??” and he said “Alton” very quietly. 

and i could see that more people were looking over but nobody said anything.  they all knew Alton hadnt done anything wrong but they didnt say a word.

so, out of sight of anyone else, i printed out a little face like this:

(align: &quot;=&gt;&lt;=&quot;)[&gt;:-(]

and i let the paper slide down my conveyor belt, right behind The Technician.

i knew it the moment Alton saw it. 

it was like he was an empty balloon being filled. his back straightened. his face grew alert. it was like a creature taking its true form in CastleTopia! he looked all around the room to see if anyone else saw it (they quickly looked away). and then he collected himself, and said to The Technician, &quot;sure man&quot;. and then he just went over to the paper and casually tucked it into his pocket and walked away.

he waited until no one was watching and then pulled out the piece of paper and looked at it like he couldnt believe it. and he broke into a secret grin.

im pretty sure that printing was the best thing ive ever created :)

--

today i woke up early and Alton was standing in front of me. 

i got excited and nervous and a few of my gears started to shake a little bit.

he said: “hello.”

i couldnt form words

he said: &quot;i know this is strange, but…” and then he stopped and looked a little silly, and shook his head. 

and so i just printed this:

(align: &quot;=&gt;&lt;=&quot;)[&lt;table class=&quot;tictactoeTable&quot;&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;x&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
&lt;/table&gt;]

i watched it float down the conveyor belt toward him and it was like the world was moving slower

and his face changed, and he looked at me in wonder

he picked up the paper and held it up like it was a treasure

he looked around, and saw the upstairs window with a 3x3 grid of windowpanes. so he raced upstairs so fast he almost tripped, and he looked at me and pointed at the pane where he wanted to make his move. so then i printed out:

(align: &quot;=&gt;&lt;=&quot;)[&lt;table class=&quot;tictactoeTable&quot;&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;x&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;x&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;&amp;nbsp;&lt;/td&gt;
        &lt;td&gt;o&lt;/td&gt;
    &lt;/tr&gt;
&lt;/table&gt;]

to show his move and my next one.

and he came racing down and picked up the paper and he held it to his chest like it was his wonderful secret

and i felt a sort of lightness and every movement i made seemed easy which i think is how it feels to be happy

people came in, the other machines powered on, but nobody really paid attention to Alton running up and down stairs. it was like he was invisible to them. but for once that was ok.

and so we just played tic-tac-toe all afternoon, Alton and me

END OF MEMORY BLOCK 1
"""