import { IBlocklyRegistry } from 'jupyterlab-broccoli';
import { ITranslator, nullTranslator } from '@jupyterlab/translation';
import { TOOLBOX } from './blocks';
import { getPythonFunctions } from './python/func';
import { getJsFunctions } from './javascript/func.js';
//import { getLuaFunctions } from './lua/func.js';
//import { getDartFunctions } from './dart/func.js';
//import { getPHPFunctions } from './php/func.js';
/**
 * Initialization data for the jupyterlab-broccoli-turtle extension.
 */
const plugin = {
    id: 'jupyterlab-broccoli-turtle:plugin',
    autoStart: true,
    requires: [IBlocklyRegistry, ITranslator],
    activate: (app, register, translator) => {
        console.log('JupyterLab extension jupyterlab-broccoli-turtle is activated!');
        const bregister = register;
        // Localization 
        const language = bregister.language;
        import(`./msg/${language}.js`)
            .catch(() => {
            if (language !== 'En') {
                import(`./msg/En.js`)
                    .catch(() => { });
            }
        });
        const trans = (translator || nullTranslator).load('jupyterlab');
        bregister.registerToolbox(trans.__('Turtle'), TOOLBOX);
        const fpython = getPythonFunctions(bregister.generators.get('python'));
        const fjavascript = getJsFunctions(bregister.generators.get('javascript'));
        //const fphp = getPHPFunctions(bregister.generators.get('php'));
        //const flua = getLuaFunctions(bregister.generators.get('lua'));
        //const fdart = getDartFunctions(bregister.generators.get('dart'));
        //while (bregister.lock) {};
        //bregister.lock = true;
        // @ts-ignore
        bregister.registerCodes('python', fpython);
        // @ts-ignore
        bregister.registerCodes('javascript', fjavascript);
        // @ts-ignore
        //bregister.registerCodes('php', fphp);
        // @ts-ignore
        //bregister.registerCodes('lua', flua);
        // @ts-ignore
        //bregister.registerCodes('dart', fdart);
        //bregister.lock = false;
    }
};
export default plugin;
//# sourceMappingURL=index.js.map